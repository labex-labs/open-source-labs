# Something After an Animation Completes

A common mistake when implementing jQuery effects is assuming that the execution of the next method in your chain will wait until the animation runs to completion.

```js
$("div.hidden").fadeIn(1500).addClass("lookAtMe");
```

It is important to realize that `.fadeIn()` above only kicks off the animation. Once started, the animation is implemented by rapidly changing CSS properties in a JavaScript `setInterval()` loop. When you call `.fadeIn()`, it starts the animation loop and then returns the jQuery object, passing it along to `.addClass() `which will then add the `lookAtMe` style class while the animation loop is just getting started.

To defer an action until after an animation has run to completion, you need to use an animation callback function. You can specify your animation callback as the second argument passed to any of the animation methods discussed above. For the code snippet above, we can implement a callback as follows:

```js
// Fade in all hidden paragraphs; then add a style class to them (correct with animation callback)
$("div.hidden").fadeIn(1500, function () {
  // this = DOM element which has just finished being animated
  $(this).addClass("lookAtMe");
});
```

Note that you can use the keyword this to refer to the DOM element being animated. Also note that the callback will be called for each element in the jQuery object. This means that if your selector returns no elements, your animation callback will never run! You can solve this problem by testing whether your selection returned any elements; if not, you can just run the callback immediately.

```js
// Run a callback even if there were no elements to animate
var someElement = $("#nonexistent");

var cb = function () {
  console.log("done!");
};

if (someElement.length) {
  someElement.fadeIn(300, cb);
} else {
  cb();
}
```

> You can refresh the **Web 8080** Tab to preview the web page.
