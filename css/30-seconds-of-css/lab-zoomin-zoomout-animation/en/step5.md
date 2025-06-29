# Experimenting with Animation Properties

Let's customize our animation by experimenting with different animation properties. This will help you understand how these properties affect the animation behavior.

1. Open the `style.css` file and modify the `.zoom-in-out-box` selector to try different animation properties:

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 2s ease-in-out infinite;
  /* Add a slight rotation during the animation */
  border-radius: 10px;
}
```

2. Let's understand what we changed:
   - We extended the animation duration to `2s` (2 seconds)
   - We changed the timing function to `ease-in-out` which makes both the beginning and end of the animation smooth
   - We added a `border-radius` of 10px to make the corners of our box rounded

3. Let's also modify our keyframes to add a rotation effect:

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1) rotate(0deg);
  }
  50% {
    transform: scale(1.5, 1.5) rotate(45deg);
    background-color: #2196f3;
  }
  100% {
    transform: scale(1, 1) rotate(0deg);
  }
}
```

4. In this updated keyframes definition:
   - We added a `rotate()` function to the transform property
   - At the 50% mark, the element now rotates 45 degrees while scaling up
   - We also change the background color to blue at the 50% mark

5. Save the `style.css` file after making these changes.

6. Refresh the **Web 8080** tab to see your enhanced animation.

Your animation should now be slower (2 seconds per cycle), have rounded corners, rotate while zooming, and change color halfway through the animation. This demonstrates how CSS animations can combine multiple property changes for rich visual effects.

Feel free to experiment further with different properties and values to see how they affect your animation.
