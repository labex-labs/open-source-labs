# Input With Prefix

To create an input with a visual, non-editable prefix, follow these steps:

1. Use `display: flex` to create a container element.
2. Remove the border and outline from the `<input>` field and apply them to the parent element instead to make it look like an input box.
3. Use the `:focus-within` pseudo-class selector to style the parent element accordingly when the user interacts with the `<input>` field.

Here's the code block you can use to create the input box with a prefix:

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

And here's the CSS code block that you can use to style the input box:

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