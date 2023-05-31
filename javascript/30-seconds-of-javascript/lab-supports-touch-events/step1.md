# Check if Device Supports Touch Events

To check if touch events are supported, simply check if `'ontouchstart'` exists in the `Window`. You can do this by typing `const supportsTouchEvents = () => window && 'ontouchstart' in window;` in the Terminal/SSH and running `supportsTouchEvents();`. If the output is `true`, then touch events are supported.
