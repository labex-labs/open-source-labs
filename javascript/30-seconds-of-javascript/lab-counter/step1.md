# Counter

To start practicing coding, open the Terminal/SSH and type `node`.

Use this function to create a counter with a specified range, step, and duration for a selected element.

```js
const counter = (selector, start, end, step = 1, duration = 2000) => {
  // Check if `step` has the proper sign and change it accordingly.
  let current = start,
    _step = (end - start) * step < 0 ? -step : step,
    // Use `setInterval()` in combination with `Math.abs()` and `Math.floor()` to calculate the time between each new text draw.
    timer = setInterval(() => {
      current += _step;
      // Use `Document.querySelector()`, `Element.innerHTML` to update the value of the selected element.
      document.querySelector(selector).innerHTML = current;
      if (current >= end) document.querySelector(selector).innerHTML = end;
      if (current >= end) clearInterval(timer);
    }, Math.abs(Math.floor(duration / (end - start))));
  return timer;
};
```

You can omit the fourth argument, `step`, to use a default step of `1`. You can also omit the fifth argument, `duration`, to use a default duration of `2000`ms.

Here's an example of how to use this function:

```js
counter("#my-id", 1, 1000, 5, 2000);
// Creates a 2-second timer for the element with id="my-id"
```
