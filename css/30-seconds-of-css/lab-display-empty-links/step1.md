# Style Links With No Text

`index.html` and `style.css` have already been provided in the VM.

To display the link URL for links that have no text, you can use the `:empty` pseudo-class to select such links, the `:not` pseudo-class to exclude links with text, and the `content` property in combination with the `attr()` function to display the link URL in the `::before` pseudo-element. Here's an example code snippet:

```html
<a href="https://30secondsofcode.org"></a>
```

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
