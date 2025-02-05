# Hide Scroll Bars

`index.html` and `style.css` have already been provided in the VM.

To allow an element to be scrollable while hiding the scrollbars, follow these steps:

- Use `overflow: auto` to enable scrolling on the element.
- Use `scrollbar-width: none` to hide the scrollbars on Firefox.
- Use `display: none` on the `::-webkit-scrollbar` pseudo-element to hide the scrollbars on WebKit browsers (such as Chrome, Edge, and Safari).

Here's an example implementation:

```html
<div class="scrollable">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
.scrollable {
  width: 200px;
  height: 100px;
  overflow: auto;
  scrollbar-width: none;
}

/* Hide scrollbars on WebKit browsers */
.scrollable::-webkit-scrollbar {
  display: none;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
