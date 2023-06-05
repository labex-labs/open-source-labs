# Focus Within

To change the appearance of a form if any of its children are focused, use the pseudo-class `:focus-within` to apply styles to a parent element if any child element gets focused. The code can be written in `index.html` and `style.css`. 

Here's an example:

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