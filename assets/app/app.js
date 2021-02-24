// This still produces an app.css file in the end. We're importing our CSS here
// to avoid having to wait 5+ seconds for Webpack to pick up changes when we
// add custom styles / imports to app.css.
import './tailwind/before.css';
import './app.css';
import './tailwind/after.css';
