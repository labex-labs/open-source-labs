# Show Additional Content on Hover

`index.html` and `style.css` have already been provided in the VM.

To create a card that displays additional content on hover, follow these steps:

1. Use `overflow: hidden` on the card to hide any elements that overflow vertically.
2. Use the `:hover` and `:focus-within` pseudo-class selectors to change the card's styling when the element is hovered, focused, or any of its descendants are focused.
3. Set `transition: 0.3s ease all` to create a smooth transition effect on hover/focus.

Here is an example HTML code for the card:

```html
<div class="card">
  <img src="https://picsum.photos/id/404/367/267" />
  <h3>Lorem ipsum</h3>
  <div class="focus-content">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br />
      <a href="#">Link to source</a>
    </p>
  </div>
</div>
```

And here is the CSS code to style the card:

```css
.card {
  width: 300px;
  height: 280px;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  width: 300px;
  height: 224px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card .focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img,
.card:focus-within img {
  margin-top: -80px;
}

.card:hover h3,
.card:focus-within h3 {
  padding: 8px 12px 0;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
