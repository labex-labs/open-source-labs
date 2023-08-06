# Hamburger Button

`index.html` and `style.css` have already been provided in the VM.

To create a hamburger menu that transitions to a cross button on hover, follow these steps:

1. Use a `.hamburger-menu` container `div` which contains the top, bottom, and middle bars.
2. Set the container to `display: flex` with `flex-flow: column wrap`.
3. Add distance between the bars using `justify-content: space-between`.
4. Use `transform: rotate()` to rotate the top and bottom bars by 45 degrees and `opacity: 0` to fade the middle bar on hover.
5. Use `transform-origin: left` so that the bars rotate around the left point.

Here's the corresponding HTML code:

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

And here's the CSS code:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
