# Box-Sizing Reset

This code block contains the necessary code to reset the box-model and ensure that the `width` and `height` properties are not affected by `border` or `padding`. 

To achieve this:

- Set `box-sizing: border-box` to include the width and height of `padding` and `border` when calculating the element's `width` and `height`.
- Use `box-sizing: inherit` to pass down the `box-sizing` property from parent to child elements.

Here's an example code block:

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
}

.content-box {
  box-sizing: content-box;
}
``` 

Note that the `box-sizing` property is set to `border-box` for all `div` elements, and then overridden for the `.content-box` class with a value of `content-box`. The `*` selector, along with `::before` and `::after` pseudo-elements, is used to ensure that all elements inherit the `box-sizing` property from their parent elements.