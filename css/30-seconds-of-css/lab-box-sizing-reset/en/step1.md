# Box-Sizing Reset

`index.html` and `style.css` have already been provided in the VM.

To ensure that the `width` and `height` of an element are not affected by `border` or `padding`, use the `box-sizing: border-box` CSS property. This includes the `padding` and `border` in the calculation of the element's `width` and `height`. If you want to inherit the `box-sizing` property from a parent element, use `box-sizing: inherit`.

Here's an example of using `box-sizing` property with two `div` elements:

```html
<div class="box">border-box</div>
<div class="box content-box">content-box</div>
```

```css
*,
*::before,
*::after {
  box-sizing: inherit;
}

.box {
  display: inline-block;
  width: 120px;
  height: 120px;
  padding: 8px;
  margin: 8px;
  background: #f24333;
  color: white;
  border: 1px solid #ba1b1d;
  border-radius: 4px;
  box-sizing: border-box;
}

.content-box {
  box-sizing: content-box;
}
```

In this example, the first `div` element has `box-sizing: border-box`, and the second `div` element has `box-sizing: content-box`.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
