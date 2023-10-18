# Evenly Distributed Children

`index.html` and `style.css` have already been provided in the VM.

To evenly distribute child elements within a parent element, use the flexbox layout by setting the parent element's display property to `flex`. To distribute the children horizontally with equal space between them, use `justify-content: space-between`. To distribute the children with space around them, use `justify-content: space-around`. Here's an example:

```html
<div class="evenly-distributed-children">
  <p>Item1</p>
  <p>Item2</p>
  <p>Item3</p>
</div>
```

```css
.evenly-distributed-children {
  display: flex;
  justify-content: space-between;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
