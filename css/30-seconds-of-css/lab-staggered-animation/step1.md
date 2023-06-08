# Staggered Animation

`index.html` and `style.css` have already been provided in the VM.

This code creates a staggered animation for a list's elements. To do this:

1. Make the list elements transparent and move them all the way to the right by setting `opacity: 0` and `transform: translateX(100%)`.
2. Specify the same `transition` properties for list elements, except `transition-delay`.
3. Use inline styles to specify a value for `--i` for each list element. This will be used for `transition-delay` to create the stagger effect.
4. Use the `:checked` pseudo-class selector for the checkbox to style list elements. To make them appear and slide into view, set `opacity` to `1` and `transform` to `translateX(0)`.

Here is the HTML and CSS code to achieve this effect:

```html
<div class="container">
  <input type="checkbox" name="menu" id="menu" class="menu-toggler">
  <label for="menu" class="menu-toggler-label">Menu</label>
  <ul class="stagger-menu">
    <li style="--i: 0">Home</li>
    <li style="--i: 1">Pricing</li>
    <li style="--i: 2">Account</li>
    <li style="--i: 3">Support</li>
    <li style="--i: 4">About</li>
  </ul>
</div>
```

```css
.container {
  overflow-x: hidden;
  width: 100%;
}

.menu-toggler {
  display: none;
}

.menu-toggler-label {
  cursor: pointer;
  font-size: 20px;
  font-weight: bold;
}

.stagger-menu {
  list-style-type: none;
  margin: 16px 0;
  padding: 0;
}

.stagger-menu li {
  margin-bottom: 8px;
  font-size: 18px;
  opacity: 0;
  transform: translateX(100%);
  transition: opacity 0.3s cubic-bezier(0.750, -0.015, 0.565, 1.055), transform 0.3s cubic-bezier(0.750, -0.015, 0.565, 1.055);
}

.menu-toggler:checked ~ .stagger-menu li {
  opacity: 1;
  transform: translateX(0);
  transition-delay: calc(0.055s * var(--i));
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
