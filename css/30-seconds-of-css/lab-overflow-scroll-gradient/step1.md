# Overflow Scroll Gradient

`index.html` and `style.css` have already been provided in the VM.

To add a fading gradient to an overflowing element and indicate that there is more content to be scrolled, follow these steps:

1. Use the `::after` pseudo-element to create a `linear-gradient()` that fades from `transparent` to `white` (top to bottom).
2. Position and size the pseudo-element in its parent using `position: absolute`, `width`, and `height`.
3. Exclude the pseudo-element from mouse events by using `pointer-events: none`, allowing text behind it to still be selectable/interactive.

Here is an example HTML and CSS code snippet:

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
