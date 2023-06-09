# Perspective Transform on Hover

`index.html` and `style.css` have already been provided in the VM.

To create a perspective transform with a hover animation on an element:

1. Use the `transform` property with the `perspective()` and `rotateY()` functions to apply a perspective to the element. For example, to create a left perspective, use `transform: perspective(1500px) rotateY(15deg);`. To create a right perspective, use `transform: perspective(1500px) rotateY(-15deg);`.

2. Use the `transition` property to animate the `transform` property when the element is hovered. For example, `transition: transform 1s ease 0s;`.

3. To mirror the perspective effect from left to right, change the `rotateY()` value to negative on the right perspective. For example, use `transform: perspective(1500px) rotateY(-15deg);`.

Example HTML:

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

Example CSS:

```css
.image-card {
  display: inline-block;
  box-sizing: border-box;
  margin: 1rem;
  width: 240px;
  height: 320px;
  padding: 8px;
  border-radius: 1rem;
  background: url("https://picsum.photos/id/1049/240/320");
  box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
}

.perspective-left {
  transform: perspective(1500px) rotateY(15deg);
  transition: transform 1s ease 0s;
}

.perspective-left:hover {
  transform: perspective(3000px) rotateY(5deg);
}

.perspective-right {
  transform: perspective(1500px) rotateY(-15deg);
  transition: transform 1s ease 0s;
}

.perspective-right:hover {
  transform: perspective(3000px) rotateY(-5deg);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
