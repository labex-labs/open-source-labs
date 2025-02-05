# Changing Display Based on Current Visibility State

jQuery can also let you change a content's visibility based on its current visibility state. `.toggle()` will show content that is currently hidden and hide content that is currently visible. You can pass the same arguments to `.toggle()` as you pass to any of the effects methods above.

```js
// Instantaneously toggle the display of all paragraphs
$("p").toggle();

// Toggle the display of all divs over 1.8 seconds
$("div").toggle(1800);
```

`.toggle()` will use a combination of slide and fade effects, just as `.show()` and `.hide()` do.

> You can refresh the **Web 8080** Tab to preview the web page.
