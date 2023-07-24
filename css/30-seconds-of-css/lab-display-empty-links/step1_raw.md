# Style Links With No Text

Displays the link URL for links with no text.

- Use the `:empty` pseudo-class to select links with no text.
- Use the `:not` pseudo-class to exclude links with text.
- Use the `content` property and the `attr()` function to display the link URL in the `::before` pseudo-element.

```html
<a href="https://30secondsofcode.org"></a>
```

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```
