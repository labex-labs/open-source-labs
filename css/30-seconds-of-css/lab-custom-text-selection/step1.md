# Custom Text Selection

`index.html` and `style.css` have already been provided in the VM.

Revised: To modify the style of selected text, utilize the `::selection` pseudo-selector. Here's an example code snippet to select and style text within a paragraph element:

```html
<p class="custom-text-selection">Select some of this text.</p>
```

```css
::selection {
  background: aquamarine;
  color: black;
}

.custom-text-selection::selection {
  background: deeppink;
  color: white;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
