# Fallback for Images That Fail to Load

`index.html` and `style.css` have already been provided in the VM.

When an image fails to load, display an error message to the user. To do this, apply styles to the `img` element as if it were a text container, setting its display to block and its width to 100%. Use the `::before` and `::after` pseudo-elements to respectively display the error message and the image URL. These elements will only be shown if the image fails to load.

Here's an example code snippet:

```html
<img src="https://nowhere.to.be/found.jpg" />
```

```css
img {
  display: block;
  width: 100%;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  font-family: sans-serif;
  font-weight: 300;
}

img::before {
  content: "Sorry, this image is unavailable.";
  display: block;
  margin-bottom: 8px;
}

img::after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
