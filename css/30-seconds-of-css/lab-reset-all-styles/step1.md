# Reset All Styles

`index.html` and `style.css` have already been provided in the VM.

To reset all styles to their default values, use the `all` property. This property will not affect the `direction` and `unicode-bidi` properties. Here's an example of how to use it:

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

```css
.reset-all-styles {
  all: initial;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
