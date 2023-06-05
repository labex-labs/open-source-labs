# How to Create a Stripes Background Pattern

To create a stripes background pattern, follow these steps:

1. In the `index.html` and `style.css` files, write the following code:

```html
<div class="stripes"></div>
```

```css
.stripes {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(90deg, transparent 50%, #000 50%);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

2. Use the `background-color` property to set the background to white.

3. Use the `background-image` property with a `linear-gradient()` value to create vertical stripes. 

4. Use the `background-size` property to specify the size of the pattern.

Note that the fixed `height` and `width` of the element is for demonstration purposes only.