"""ninja 的api入口"""

import json
import os
import re
from typing import Any, Mapping, Type

from django.conf import settings
from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Field, NinjaAPI, Schema
from ninja.pagination import PaginationBase
from ninja.renderers import BaseRenderer
from ninja.responses import NinjaJSONEncoder


class CustomRenderer(BaseRenderer):
    """
    在原版的基础上给外层包裹'data'
    """

    media_type = "application/json"
    encoder_class: Type[json.JSONEncoder] = NinjaJSONEncoder
    json_dumps_params: Mapping[str, Any] = {}

    def render(
        self, request: HttpRequest, data: Any, *, response_status: int
    ) -> Any:
        if response_status == 200:
            response_content = {"data": data}
        elif response_status in (400, 422, 404):
            # 确保data是字典格式
            if not isinstance(data, dict):
                data = {"detail": data}
            data["errorCode"] = response_status
            response_content = {"error": data}
        else:
            # 其他错误状态的处理或者默认错误处理
            response_content = {
                "error": {
                    "detail": "An error occurred",
                    "errorCode": response_status,
                }
            }

            # 返回JSON响应
        return json.dumps(
            response_content, cls=self.encoder_class, **self.json_dumps_params
        )


class HandleHighlight:
    """
    高亮替换功能
    """

    def __init__(self, response):
        self.response = response

    @staticmethod
    def sub_em(value: list[str]):
        """
        <em>tRNA</em> 换成  <span class=high-light>tRNA</span>
        """
        # 使用 re.sub() 方法进行替换
        new_value = []
        for item in value:
            new_text = re.sub(
                r"<em>(.*?)<\/em>", r"<span class=high-light>\1</span>", item
            )
            new_value.append(new_text)

        return ",".join(new_value)  # 多个高亮字段可能有问题

    @property
    def value(self):
        """
        替换后放回原处
        """
        result = []
        for item in self.response.hits.hits:
            source = item._source
            # 如果有高亮命中，则替换 em 为 span
            if getattr(item, "highlight", None):
                highlight = item.highlight.to_dict()
                for key, value in highlight.items():
                    source[key] = self.sub_em(value)
            result.append(source)
        return result


class PGPagination(PaginationBase):
    """
    自定义符合组内规范的适用于PG的分页器
    """

    class Input(Schema):
        """url parameters中的参数"""

        page: int = Field(1, ge=1)
        per_page: int = Field(10, ge=1)

    class Output(Schema):
        """自定义分页输出的格式"""

        page: int
        per_page: int
        total: int
        items: list[Any]  # `items` is a default attribute

    def paginate_queryset(self, queryset, pagination: Input, **params):
        """
        分页函数
        """
        page = pagination.page
        per_page = pagination.per_page
        offset = (page - 1) * per_page
        if isinstance(queryset, QuerySet):
            total = queryset.count()
        else:
            total = len(queryset)
        items = queryset[offset : offset + per_page]
        return {
            "items": items,
            "page": page,
            "per_page": per_page,
            "total": total,
        }


PROJECT_CODE = os.getenv("PROJECT_CODE", "horizon365")
ninja_api = NinjaAPI(
    title=f"{PROJECT_CODE} 文档中心",
    renderer=CustomRenderer(),
    docs_url="/docs" if settings.DEBUG else None,  # 在线文档线上不可用
    openapi_url="/openapi.json"
    if settings.DEBUG
    else None,  # open.json线上不可用
    openapi_extra={},
)
