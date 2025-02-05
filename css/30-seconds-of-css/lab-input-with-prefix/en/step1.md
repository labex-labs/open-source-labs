# Input With Prefix

`index.html` and `style.css` have already been provided in the VM.

To create an input with a visual, non-editable prefix, follow these steps:

1. Use `display: flex` to create a container element with the class `.input-box`.
2. Remove the border and outline from the `<input>` field and apply them to the parent element instead to make it look like an input box.
3. Use the `:focus-within` pseudo-class selector to style the parent element accordingly when the user interacts with the `<input>` field.

Here is the HTML code:

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

And here is the CSS code:

```css
.input-box {
  display: flex;
  align-items: center;
  max-width: 300px;
  background: #fff;
  border: 1px solid #a0a0a0;
  border-radius: 4px;
  padding-left: 0.5rem;
  overflow: hidden;
  font-family: sans-serif;
}

.input-box .prefix {
  font-weight: 300;
  font-size: 14px;
  color: #999;
}

.input-box input {
  flex-grow: 1;
  font-size: 14px;
  background: #fff;
  border: none;
  outline: none;
  padding: 0.5rem;
}

.input-box:focus-within {
  border-color: #777;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
