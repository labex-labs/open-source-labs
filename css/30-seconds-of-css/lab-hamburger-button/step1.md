# Hamburger Button

To create a hamburger button that transitions to a cross button on hover, follow these steps:

1. Add a `.hamburger-menu` container `div` that contains three bars - top, middle, and bottom.
2. Set the container to `display: flex` with `flex-flow: column wrap` to ensure that the bars are aligned vertically.
3. Add distance between the bars using `justify-content: space-between`.
4. Set the height and width of the container to `2.5rem` to ensure that the button is of a reasonable size.
5. Set `cursor: pointer` to indicate that the button is clickable.
6. Set the height, background, border radius, and margin of the bars using `.hamburger-menu .bar` selector.
7. Set `transform-origin: left` so that the bars rotate around the left point.
8. Set `transition: all 0.5s` to ensure that the animation is smooth.
9. Use `transform: rotate()` to rotate the top and bottom bars by 45 degrees and `opacity: 0` to fade the middle bar on hover.

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

```css
.hamburger-menu {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  height: 2.5rem;
  width: 2.5rem;
  cursor: pointer;
}

.hamburger-menu .bar {
  height: 5px;
  background: black;
  border-radius: 5px;
  margin: 3px 0px;
  transform-origin: left;
  transition: all 0.5s;
}

.hamburger-menu:hover .top {
  transform: rotate(45deg);
}

.hamburger-menu:hover .middle {
  opacity: 0;
}

.hamburger-menu:hover .bottom {
  transform: rotate(-45deg);
}
```