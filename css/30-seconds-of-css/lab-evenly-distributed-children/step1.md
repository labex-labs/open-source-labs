# Evenly Distributed Children

To evenly distribute child elements within a parent element, follow the steps below:

1. Open `index.html` and `style.css`.

2. Use `display: flex` in the CSS to apply the flexbox layout to the parent element.

3. Use `justify-content: space-between` to evenly distribute child elements horizontally. This will position the first item at the left edge and the last item at the right edge.

4. Alternatively, use `justify-content: space-around` to distribute the children with space around them, instead of between them.

Here's an example code block to help you get started:

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
