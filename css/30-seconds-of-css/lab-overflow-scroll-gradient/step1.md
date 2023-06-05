# Overflow Scroll Gradient

This code block adds a gradient effect to an overflowing element to indicate that there is more content available to be scrolled. The `index.html` and `style.css` files should be used to write the code.

To implement this effect, follow these steps:

1. Use the `::after` pseudo-element to create a `linear-gradient()` that fades from `transparent` to `white` (top to bottom).
2. Use `position: absolute`, `width` and `height` to place and size the pseudo-element in its parent.
3. Use `pointer-events: none` to exclude the pseudo-element from mouse events, so that text behind it remains selectable/interactive.

The following code can be used in your `index.html` file:

```html
<div class="overflow-scroll-gradient">
  <div class="overflow-scroll-gradient-scroller">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. <br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit? <br />
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </div>
</div>
```

And this code can be used in your `style.css` file:

```css
.overflow-scroll-gradient {
  position: relative;
}

.overflow-scroll-gradient::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 250px;
  height: 25px;
  background: linear-gradient(transparent, white);
  pointer-events: none;
}

.overflow-scroll-gradient-scroller {
  overflow-y: scroll;
  background: white;
  width: 240px;
  height: 200px;
  padding: 15px;
  line-height: 1.2;
}
```