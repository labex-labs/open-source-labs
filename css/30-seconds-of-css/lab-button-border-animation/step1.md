# Button Border Animation

This code creates a border animation on hover for a button. The code is written in `index.html` and `style.css`.

To create the animation:
- Two boxes `24px` wide will be created using `::before` and `::after` pseudo-elements, positioned above and below the button.
- On hover, the `width` of the boxes will extend to `100%` and the change will be animated using `transition`.

Here is the code:

```html
<button class="animated-border-button">Submit</button>
```

```css
.animated-border-button {
  background-color: #263059;
  border: none;
  color: #ffffff;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
}

.animated-border-button::before,
.animated-border-button::after {
  border: 0 solid transparent;
  transition: all 0.3s;
  content: "";
  height: 0;
  position: absolute;
  width: 24px;
}

.animated-border-button::before {
  border-top: 2px solid #263059;
  right: 0;
  top: -4px;
}

.animated-border-button::after {
  border-bottom: 2px solid #263059;
  bottom: -4px;
  left: 0;
}

.animated-border-button:hover::before,
.animated-border-button:hover::after {
  width: 100%;
}
```