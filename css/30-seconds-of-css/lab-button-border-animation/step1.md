# Button Border Animation

`index.html` and `style.css` have already been provided in the VM.

Revised:

To create a border animation on hover, you can use the `::before` and `::after` pseudo-elements to generate two boxes that are `24px` wide and positioned above and below the box. Then, apply the `:hover` pseudo-class to increase the `width` of those elements to `100%` on hover and animate the transition using `transition`.

Here's an example code snippet:

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
  content: '';
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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
