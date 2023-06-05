# Custom Navigation Item Hover and Focus Effect

This code block creates a custom hover and focus effect for navigation items using CSS transformations. The effect is achieved with the following steps:

1. Add the `::before` pseudo-element to the list item anchor to create a hover effect. Hide it using `transform: scale(0)`.
2. Use the `:hover` and `:focus` pseudo-class selectors to transition the pseudo-element to `transform: scale(1)` and show its colored background.
3. Use `z-index` to ensure that the pseudo-element does not cover the anchor element.

To implement this effect, add the following HTML code to your `index.html` file:

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

Then, add the following CSS code to your `style.css` file:

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

li a::before {
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

li a:hover::before,
li a:focus::before {
  transform: scale(1);
}
```