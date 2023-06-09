# Shifting Card

`index.html` and `style.css` have already been provided in the VM.

To create a card that shifts on hover, follow these steps:

1. Set the appropriate `perspective` on the `.container` element to allow for the shifting effect.
2. Add a `transition` for the `transform` property of the `.card` element.
3. Use `Document.querySelector()` to select the `.card` element and add event listeners for the `mousemove` and `mouseout` events.
4. Use `Element.getBoundingClientRect()` to get the `x`, `y`, `width`, and `height` of the `.card` element.
5. Calculate the relative distance as a value between `-1` and `1` for the `x` and `y` axes and apply it through the `transform` property.

Here is the sample HTML and CSS code for the card:

```html
<div class="container">
  <div class="shifting-card">
    <div class="content">
      <h3>Card</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti
        repellat, consequuntur doloribus voluptate esse iure?
      </p>
    </div>
  </div>
</div>
```

```css
.container {
  display: flex;
  padding: 24px;
  justify-content: center;
  align-items: center;
  background: #f3f1fe;
  perspective: 1000px;
}

.shifting-card {
  width: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  margin: 0.5rem;
  transition: transform 0.2s ease-out;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.shifting-card .content {
  text-align: center;
  margin: 2rem;
  line-height: 1.5;
  color: #101010;
}
```

And here is the JavaScript code to add the hover effect:

```js
const card = document.querySelector(".shifting-card");
const { x, y, width, height } = card.getBoundingClientRect();
const cx = x + width / 2;
const cy = y + height / 2;

const handleMove = (e) => {
  const { pageX, pageY } = e;
  const dx = (cx - pageX) / (width / 2);
  const dy = (cy - pageY) / (height / 2);
  e.target.style.transform = `rotateX(${10 * dy * -1}deg) rotateY(${
    10 * dx
  }deg)`;
};

const handleOut = (e) => {
  e.target.style.transform = "initial";
};

card.addEventListener("mousemove", handleMove);
card.addEventListener("mouseout", handleOut);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
