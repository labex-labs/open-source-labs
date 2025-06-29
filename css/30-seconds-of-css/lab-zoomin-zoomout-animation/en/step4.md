# Applying the Animation

Now that we have defined our keyframes, we need to apply the animation to our box element.

1. Open the `style.css` file again and modify the `.zoom-in-out-box` selector as follows:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}
```

2. Let's understand the animation property we added:
   - `animation` is a shorthand property that sets multiple animation properties at once
   - `zoom-in-zoom-out` is the name of our keyframes animation
   - `1s` specifies that one cycle of the animation lasts 1 second
   - `ease` is the timing function that makes the animation start slowly, speed up, and then slow down again
   - `infinite` means the animation will repeat forever

3. Save the `style.css` file after making these changes.

4. If the web server is already running, simply refresh the **Web 8080** tab. If not, click on "Go Live" in the bottom right corner to start the server, then open the **Web 8080** tab.

You should now see your pink square smoothly zooming in and out in a continuous animation. The square grows larger until it reaches 1.5 times its original size, then shrinks back to normal. This cycle repeats infinitely.
