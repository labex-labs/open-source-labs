# Completing the Checkerboard Pattern

Now let's add the second linear gradient to complete our checkerboard pattern and make it repeatable across the entire element.

1. Open the `style.css` file again.

2. Modify the `.checkerboard` class to include a second linear gradient that will create the alternating pattern:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ),
    linear-gradient(
      -45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    );
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

What we've added:

- A second `linear-gradient()` that is similar to the first but with a `-45deg` angle to create the alternating pattern
- The `background-repeat: repeat` property ensures that the patterns repeat across the entire element

The combination of these two gradients at different angles creates the classic checkerboard pattern. The first gradient creates one set of diagonal squares, while the second gradient creates another set that fills in the gaps.

3. Save the `style.css` file.

4. Refresh the **Web 8080** tab to see the final result.

You should now see a complete checkerboard pattern with alternating black and white squares. The pattern should repeat across the entire 240px by 240px element.

## How the Pattern Works

The checkerboard effect is created by:

1. Using two linear gradients with opposite angles (45deg and -45deg)
2. Each gradient creates a pattern of black squares at the corners
3. The transparent areas allow the white background to show through
4. The `background-size` property controls the size of each square in the pattern
5. The `background-repeat` property makes the pattern repeat across the entire element

This technique demonstrates the power of CSS gradients for creating complex patterns without the need for image files, resulting in faster loading times and better scalability.
