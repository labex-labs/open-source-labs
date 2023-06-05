# Hiding Empty Elements

To hide elements with no content, use the `:empty` pseudo-class to select them.

Here's an example of how to use it:

```html
<p>Lorem ipsum dolor sit amet. <button></button></p>
```

```css
:empty {
  display: none;
}
```

In this example, any element with no content (such as the button in the paragraph) will be hidden. You can write this code in `index.html` and `style.css`.
