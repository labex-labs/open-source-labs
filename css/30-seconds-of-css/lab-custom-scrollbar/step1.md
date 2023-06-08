# Custom Scrollbar

`index.html` and `style.css` have already been provided in the VM.

To customize the scrollbar style for elements with scrollable overflow, you can use `::-webkit-scrollbar` to style the scrollbar element, `::-webkit-scrollbar-track` to style the scrollbar track (the background of the scrollbar), and `::-webkit-scrollbar-thumb` to style the scrollbar thumb (the draggable element). However, note that this technique only works on WebKit-based browsers, and scrollbar styling is not on any standards track. Here is an example of how to use these selectors in HTML and CSS:

```html
<div class="custom-scrollbar">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.custom-scrollbar {
  height: 70px;
  overflow-y: scroll;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #1E3F20;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #4A7856;
  border-radius: 12px;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
