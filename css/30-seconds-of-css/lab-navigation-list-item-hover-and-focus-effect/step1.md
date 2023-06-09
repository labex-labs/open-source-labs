# Navigation List Item Hover and Focus Effect

`index.html` and `style.css` have already been provided in the VM.

To create a custom hover and focus effect for navigation items, use CSS transformations as follows:

1. Use the `::before` pseudo-element at the list item anchor to create a hover effect. Hide it using `transform: scale(0)`.
2. Use the `:hover` and `:focus` pseudo-class selectors to transition the pseudo-element to `transform: scale(1)` and show its colored background.
3. Prevent the pseudo-element from covering the anchor element by using `z-index`.

You can use the following HTML code for your navigation menu:

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

And apply the following CSS rules:

```css
.hover-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.hover-nav li {
  float: left;
}

.hover-nav li a {
  position: relative;
  display: block;
  color: #fff;
  text-align: center;
  padding: 8px 12px;
  text-decoration: none;
  z-index: 0;
}

.hover-nav li a::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: #2683f6;
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

.hover-nav li a:hover::before,
.hover-nav li a:focus::before {
  transform: scale(1);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
