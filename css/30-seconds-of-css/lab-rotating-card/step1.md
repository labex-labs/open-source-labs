# Rotating Card

`index.html` and `style.css` have already been provided in the VM.

To create a two-sided card that rotates on hover, follow these steps:

1. Set the `backface-visibility` of the cards to `none` to prevent the backside from being visible by default.
2. Initially, set `rotateY(-180deg)` for the back side of the card and `rotateY(0deg)` for the front side of the card.
3. Upon hover, set `rotateY(180deg)` for the front side of the card and `rotateY(0deg)` for the back side of the card.
4. Set the appropriate `perspective` value to create the rotate effect.

Here is an example HTML and CSS code:

```html
<div class="card">
  <div class="card-side front">
    <div>Front Side</div>
  </div>
  <div class="card-side back">
    <div>Back Side</div>
  </div>
</div>
```

```css
.card {
  perspective: 150rem;
  position: relative;
  height: 40rem;
  max-width: 400px;
  margin: 2rem;
  box-shadow: none;
  background: none;
}

.card-side {
  height: 35rem;
  border-radius: 15px;
  transition: all 0.8s ease;
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  padding: 2rem;
  color: white;
}

.card-side.back {
  transform: rotateY(-180deg);
  background: linear-gradient(43deg, #4158d0 0%, #c850c0 46%, #ffcc70 100%);
}

.card-side.front {
  background: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover .card-side.front {
  transform: rotateY(180deg);
}

.card:hover .card-side.back {
  transform: rotateY(0deg);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
