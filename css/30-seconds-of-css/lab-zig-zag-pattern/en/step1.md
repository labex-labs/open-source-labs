# Zig Zag Background Pattern

`index.html` and `style.css` have already been provided in the VM.

To create a zig zag background pattern, use the following steps:

1. Set a white background using `background-color`.
2. Create the parts of a zig zag pattern using `background-image` with four `linear-gradient()` values.
3. Specify the pattern's size using `background-size`.
4. Place the parts of the pattern in the correct locations using `background-position`.
5. To repeat the pattern, use `background-repeat`.
6. **Note:** The `height` and `width` of the element are fixed for demonstration purposes only.

Here is an example code snippet:

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%),
    linear-gradient(315deg, #000 25%, transparent 25%),
    linear-gradient(45deg, #000 25%, transparent 25%);
  background-position:
    -30px 0,
    -30px 0,
    0 0,
    0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
