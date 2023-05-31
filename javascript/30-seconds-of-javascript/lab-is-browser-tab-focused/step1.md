# How to Check if Browser Tab Is Focused

To check whether the browser tab is focused, you can use the `Document.hidden` property. This property is part of the Page Visibility API. It lets you determine if the browser tab of the page is visible or hidden.

Here's an example code snippet you can use to check if the browser tab is focused:

```js
const isBrowserTabFocused = () => !document.hidden;
```

To use this function, simply call `isBrowserTabFocused()`. It will return `true` if the browser tab is focused, and `false` if it's not.
