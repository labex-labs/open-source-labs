# Disable Selection

`index.html` and `style.css` have already been provided in the VM.

To make an element's content unselectable, add the CSS property `user-select: none` to the selector. However, this method is not entirely secure to prevent users from copying content.

Example:

```html
<p>You can select me.</p>
<p class="unselectable">You can't select me!</p>
```

```css
.unselectable {
  user-select: none;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
