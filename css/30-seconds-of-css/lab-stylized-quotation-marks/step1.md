# Customizing Stylized Quotation Marks

To customize the style of inline quotation marks, use the `quotes` property to customize the characters used for the opening and closing quotes of a `<q>` element. The code for the HTML and CSS files are `index.html` and `style.css`, respectively.

Here's an example code snippet:

```html
<p><q>Do or do not, there is no try.</q> – Yoda</p>
```

```css
q {
  quotes: "“" "”";
}
```