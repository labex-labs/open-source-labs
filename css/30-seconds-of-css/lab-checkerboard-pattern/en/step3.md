# Creating the First Gradient

Now we'll start creating our checkerboard pattern using CSS gradients. Let's add the first linear gradient to create part of the pattern.

## Understanding CSS Linear Gradients

CSS linear gradients allow you to create smooth transitions between two or more colors in a straight line. The `linear-gradient()` function takes an angle and a series of color stops as parameters. We'll use this technique to create our checkerboard squares.

Follow these steps:

1. Open the `style.css` file.

2. Let's modify our `.checkerboard` class to include the first linear gradient:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(
    45deg,
    #000 25%,
    transparent 25%,
    transparent 75%,
    #000 75%,
    #000
  );
  background-size: 60px 60px;
}
```

Let me explain what this gradient does:

- `45deg` specifies the angle of the gradient
- `#000 25%` creates a black color from 0% to 25% of the available space
- `transparent 25%` creates a transparent color starting at 25%
- `transparent 75%` maintains the transparent color until 75%
- `#000 75%` transitions back to black at 75% and continues to the end
- `background-size: 60px 60px` sets the size of each repeating gradient cell

3. Save the `style.css` file.

4. Refresh the **Web 8080** tab to see the changes.

You should now see a pattern starting to form, but it's not a complete checkerboard yet. The first gradient creates only a portion of the pattern. In the next step, we'll add a second gradient to complete the checkerboard.
