# Button Swing Animation

`index.html` and `style.css` have already been provided in the VM.

To create a swing animation on focus, you should use an appropriate `transition` to animate changes to the element. Then, apply the `:focus` pseudo-class to the element and use `animation` with `transform` to make it swing. Finally, add `animation-iteration-count` to play the animation only once. Here is an example of how to do this in HTML and CSS:

```html
<button class="button-swing">Submit</button>
```

```css
.button-swing {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button-swing:focus {
  animation: swing 1s ease;
  animation-iteration-count: 1;
}

@keyframes swing {
  15% {
    transform: translateX(5px);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(3px);
  }
  65% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  100% {
    transform: translateX(0);
  }
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
