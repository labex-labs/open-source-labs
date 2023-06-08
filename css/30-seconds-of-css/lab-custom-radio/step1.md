# Custom Radio Button

This code creates a styled radio button with animation on state change. To use it, follow these steps:

1. Create a `.radio-container` element using flexbox to create the appropriate layout for the radio buttons.
2. Reset the styles on the `<input>` and use it to create the outline and background of the radio button.
3. Use the `::before` pseudo-element to create the inner circle of the radio button.
4. Use `transform: scale(1)` and a CSS transition to create an animation effect on state change.

Here's the code you need to add to your `index.html` and `style.css` files:

```html
<div class="radio-container">
  <input class="radio-input" id="apples" type="radio" name="fruit" />
  <label class="radio" for="apples">Apples</label>
  <input class="radio-input" id="oranges" type="radio" name="fruit" />
  <label class="radio" for="oranges">Oranges</label>
</div>
```

```css
.radio-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  height: 64px;
  background-color: #ffffff;
  color: #222;
}

.radio-container * {
  box-sizing: border-box;
}

.radio-input {
  appearance: none;
  width: 16px;
  height: 16px;
  margin: 0;
  border-radius: 50%;
  border: 1px solid #cccfdb;
  background-color: #ffffff;
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-input::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: scale(0);
  transition: transform 0.3s ease-in-out;
  box-shadow: inset 6px 6px #ffffff;
}

.radio-input:checked {
  background-color: #0077ff;
  border-color: #0077ff;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio {
  cursor: pointer;
  padding: 6px 8px;
}

.radio:not(:last-child) {
  margin-right: 6px;
}
```
