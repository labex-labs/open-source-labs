# Creating the Keyframes Animation

CSS animations work by defining keyframes that specify the styles an element should have at various points during the animation sequence. Let's create the keyframes for our zoom in zoom out animation.

1. Open the `style.css` file again and add the following code at the end:

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

2. Let's understand what this code does:

   - `@keyframes` is a CSS at-rule that defines the stages and styles of an animation
   - `zoom-in-zoom-out` is the name we give to our animation (we'll reference this name later)
   - Inside the keyframes, we define what happens at different points in the animation:
     - At `0%` (the start), the element is at its normal size with `scale(1, 1)`
     - At `50%` (halfway through), the element grows to 1.5 times its size with `scale(1.5, 1.5)`
     - At `100%` (the end), the element returns to its normal size
   - The `transform` property with the `scale()` function changes the size of the element

3. Save the `style.css` file after adding these keyframes.

The keyframes define what our animation will do, but we haven't applied it to our element yet. In the next step, we'll connect the animation to our box.
