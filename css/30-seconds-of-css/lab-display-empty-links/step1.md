# Style Links With No Text

To display the link URL for links with no text, follow these steps:

1. Use the `:empty` pseudo-class to select links with no text.
2. Use the `:not` pseudo-class to exclude links with text.
3. Use the `content` property and the `attr()` function to display the link URL in the `::before` pseudo-element.

To implement this, write the code in `index.html` and `style.css`.

For example, consider the following HTML code:

```html
<a href="https://30secondsofcode.org"></a>
```

To style the above link, use the following CSS code:

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```
