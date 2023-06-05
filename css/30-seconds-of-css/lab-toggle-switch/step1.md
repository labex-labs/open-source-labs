# Toggle Switch

To create a toggle switch with CSS only, follow these steps:

1. Associate the `<label>` with the checkbox `<input>` element using the `for` attribute.
2. Use the `::after` pseudo-element of the `<label>` to create a circular knob for the switch.
3. Change the position of the knob and the `background-color` of the switch using the `:checked` pseudo-class selector with `transform: translateX(20px)`.
4. Visually hide the `<input>` element by using `position: absolute` and `left: -9999px`.

Here is the code to create the toggle switch:

```html
<input type="checkbox" id="toggle" class="offscreen" />
<label for="toggle" class="switch"></label>
```

```css
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  transition: all 0.3s;
}

.switch::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 18px;
  background-color: white;
  top: 1px;
  left: 1px;
  transition: all 0.3s;
}

input[type="checkbox"]:checked + .switch::after {
  transform: translateX(20px);
}

input[type="checkbox"]:checked + .switch {
  background-color: #7983ff;
}

.offscreen {
  position: absolute;
  left: -9999px;
}
```
