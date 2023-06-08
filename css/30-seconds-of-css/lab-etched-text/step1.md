# Etched Text

`index.html` and `style.css` have already been provided in the VM.

To create an "etched" or engraved effect for text on a background, use the following CSS properties: 

```css
.etched-text {
  text-shadow: 0 2px white;
  font-size: 1.5rem;
  font-weight: bold;
  color: #b8bec5;
}
```

The `text-shadow` property creates a white shadow offset `0px` horizontally and `2px` vertically from the origin position. Make sure that the background is darker than the shadow for the effect to work. Additionally, the text color should be slightly faded to make it look like it's been carved out of the background. Finally, apply the `etched-text` class to the desired HTML element, such as a paragraph, to achieve the effect. 

```html
<p class="etched-text">I appear etched into the background.</p>
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
