# How to Smooth-Scroll to the Top of a Page

To smooth-scroll to the top of a web page, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding practice.
2. Determine the distance from the top of the page using `Document.documentElement` or `Document.body` and `Element.scrollTop`.
3. Scroll by a fraction of the distance from the top.
4. Use `Window.requestAnimationFrame()` to animate the scrolling.

Here's an example code snippet that implements these steps:

```js
const scrollToTop = () => {
  const distanceFromTop =
    document.documentElement.scrollTop || document.body.scrollTop;
  if (distanceFromTop > 0) {
    window.requestAnimationFrame(scrollToTop);
    window.scrollTo(0, distanceFromTop - distanceFromTop / 8);
  }
};
```

To trigger the smooth-scrolling effect, simply call the `scrollToTop()` function.
