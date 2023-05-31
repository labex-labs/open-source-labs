# Check User Preference for Light Color Scheme and Open Terminal/SSH to Start Coding

To determine if the user prefers a light color scheme, use the `Window.matchMedia()` method with the appropriate media query. Here's an example code snippet:

```js
const prefersLightColorScheme = () =>
  window &&
  window.matchMedia &&
  window.matchMedia("(prefers-color-scheme: light)").matches;
```

Once you've checked the user preference, you can proceed to open the Terminal/SSH and start practicing coding by typing `node`.
