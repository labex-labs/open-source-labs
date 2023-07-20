# Hide Empty Elements

`index.html` and `style.css` have already been provided in the VM.

To hide elements with no content, use the `:empty` pseudo-class. For example, if you have the following HTML code:

```html
<p>Lorem ipsum dolor sit amet. <button></button></p>
```

You can use the following CSS code to hide the button element with no content:

```css
p:empty {
  display: none;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
