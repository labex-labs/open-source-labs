# Shake Animation on Invalid Input

To create a shake animation on invalid input, follow these steps:

1. Define the regular expression which the input's value must match using the `pattern` attribute.
2. Define a shake animation using `@keyframes` and the `margin-left` property.
3. Apply the shake animation using the `:invalid` pseudo-class.

Here's an example code snippet:

```html
<input type="text" placeholder="Letters only" pattern="[A-Za-z]*" />
```

```css
@keyframes shake {
  0% {
    margin-left: 0rem;
  }
  25% {
    margin-left: 0.5rem;
  }
  75% {
    margin-left: -0.5rem;
  }
  100% {
    margin-left: 0rem;
  }
}

input:invalid {
  animation: shake 0.2s ease-in-out 0s 2;
  box-shadow: 0 0 0.6rem #ff0000;
}
```