# Height Transition

`index.html` and `style.css` have already been provided in the VM.

This code snippet transitions an element's height from `0` to `auto` when its height is unknown by performing the following steps:

- Use the `transition` property to specify that changes to `max-height` should be transitioned over a duration of `0.3s`.
- Use the `overflow` property set to `hidden` to prevent the contents of the hidden element from overflowing its container.
- Use the `max-height` property to specify an initial height of `0`.
- Use the `:hover` pseudo-class to change the `max-height` to the value of the `--max-height` variable set by JavaScript.
- Use the `Element.scrollHeight` property and `CSSStyleDeclaration.setProperty()` method to set the value of `--max-height` to the current height of the element.
- **Note:** This approach causes reflow on each animation frame, which may cause lag when there are a large number of elements below the transitioning element.

```html
<div class="trigger">
  Hover over me to see a height transition.
  <div class="el">Additional content</div>
</div>
```

```css
.el {
  transition: max-height 0.3s;
  overflow: hidden;
  max-height: 0;
}

.trigger:hover > .el {
  max-height: var(--max-height);
}
```

```js
let el = document.querySelector(".el");
let height = el.scrollHeight;
el.style.setProperty("--max-height", height + "px");
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
