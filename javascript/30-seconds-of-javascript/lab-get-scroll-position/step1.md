# How to Get Scroll Position in JavaScript

To get the scroll position of a page in JavaScript, you can use the `getScrollPosition` function defined below. This function returns an object with the x and y coordinates of the scroll position.

```js
const getScrollPosition = (el = window) => ({
  x: el.pageXOffset !== undefined ? el.pageXOffset : el.scrollLeft,
  y: el.pageYOffset !== undefined ? el.pageYOffset : el.scrollTop,
});
```

The function checks if the `Window.pageXOffset` and `Window.pageYOffset` properties are defined and returns their values if they are. If not, it uses the `Element.scrollLeft` and `Element.scrollTop` properties to get the scroll position.

To use the `getScrollPosition` function, simply call it without any arguments to get the scroll position of the current page.

```js
getScrollPosition(); // {x: 0, y: 200}
```

You can also pass an element as an argument to get the scroll position of that element.

Note that if you omit the `el` argument, the function will use the global `Window` object by default.
