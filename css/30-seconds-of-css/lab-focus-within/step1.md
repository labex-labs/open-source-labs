# Focus Within

`index.html` and `style.css` have already been provided in the VM.

To change the appearance of a form when any of its child elements are focused, use the pseudo-class `:focus-within` to apply styles to the parent element. For example, in the given HTML code, if any of the input fields are focused, the `form` element will have a green background. To apply styles to the child elements, use appropriate CSS selectors like `label` and `input`. Here's an updated version of the code:

```html
<form>
  <label for="username">Username:</label>
  <input id="username" type="text" />
  <br />
  <label for="password">Password:</label>
  <input id="password" type="text" />
</form>
```

```css
form {
  border: 2px solid #52b882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7cf0bd;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
