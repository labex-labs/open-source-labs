# Reset All Styles

To reset all styles to their default values, use the `all` property in the `style.css` file. This will not affect the `direction` and `unicode-bidi` properties. Here's an example code block in `index.html`:

```html
<div class="reset-all-styles">
  <h5>Title</h5>
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure id
    exercitationem nulla qui repellat laborum vitae, molestias tempora velit
    natus. Quas, assumenda nisi. Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

And the corresponding CSS code:

```css
.reset-all-styles {
  all: initial;
}
```

This will reset all styles, including inherited styles, to their default values.
