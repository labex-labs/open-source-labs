# Rotating Card

This code creates a two-sided card that rotates on hover. To implement it, follow these steps:

1. In the HTML file, use the following code:

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

2. In the CSS file, use the following code:

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
  background-color: #4158d0;
  background-image: linear-gradient(
    43deg,
    #4158d0 0%,
    #c850c0 46%,
    #ffcc70 100%
  );
}

.card-side.front {
  background-color: #0093e9;
  background-image: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover .card-side.front {
  transform: rotateY(180deg);
}

.card:hover .card-side.back {
  transform: rotateY(0deg);
}
```

Make sure to:

- Set the `backface-visibility` of the cards to none.
- Initially, set `rotateY()` for the back side of the card to `-180deg` and the front side to `0deg`.
- Upon hover, set `rotateY()` for the front side to `180deg` and backside to `0deg`.
- Set the appropriate `perspective` value to create the rotate effect.