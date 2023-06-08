# Fullscreen

`index.html` and `style.css` have already been provided in the VM.

To style an element in fullscreen mode, you can use the `:fullscreen` CSS pseudo-element selector. You can also create a button that makes the element fullscreen for preview purposes using a `<button>` and `Element.requestFullscreen()`. Here's an example code:

```html
<div class="container">
  <p><em>Click the button below to enter the element into fullscreen mode. </em></p>
  <div class="element" id="element"><p>I change color in fullscreen mode!</p></div>
  <br />
  <button onclick="var el = document.getElementById('element'); el.requestFullscreen();">
    Go Full Screen!
  </button>
</div>
```

```css
.container {
  margin: 40px auto;
  max-width: 700px;
}

.element {
  padding: 20px;
  height: 300px;
  width: 100%;
  background-color: skyblue;
  box-sizing: border-box;
}

.element p {
  text-align: center;
  color: white;
  font-size: 3em;
}

/* For Internet Explorer */
.element:-ms-fullscreen p {
  visibility: visible;
}

/* For modern browsers */
.element:fullscreen {
  background-color: #e4708a;
  width: 100vw;
  height: 100vh;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
