# Creating a Card With an Image Cutout

To create a card with an image cutout, follow these steps:

1. In your `index.html` file, create a `.container` element and give it a colored background using the `background` property.
2. Inside the `.container` element, create a `.card` element and add any content you want. This should include a `figure` element containing the appropriate image for the cutout.
3. In your `style.css` file, add styles for the `.container`, `.card`, and `.content` elements.
4. To create the illusion of a cutout, use the `::before` pseudo-element to add a `border` around the `figure` element. This border should match the `.container` element's `background` color.

Here is the code you need to create the card:

```html
<div class="container">
  <div class="card">
    <figure>
      <img alt="" src="https://picsum.photos/id/447/400/400" />
    </figure>
    <p class="content">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
</div>
```

And here are the styles you need to add to your `style.css` file:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 96px 24px 48px;
  background: #f3f1fe;
}

.card {
  width: 350px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.card figure {
  width: 120px;
  height: 120px;
  margin-top: -60px;
  position: relative;
  border-radius: 50%;
}

.card figure::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  height: 100%;
  border-radius: inherit;
  border: 1rem solid #f3f1fe;
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
}

.card figure img {
  border-radius: inherit;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card .content {
  margin: 2rem;
  text-align: center;
  line-height: 1.5;
  color: #101010;
}
```