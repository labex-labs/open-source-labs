# Shake on Invalid Input

`index.html` and `style.css` have already been provided in the VM.

To create a shake animation when there is invalid input, follow these steps:

1. Use the `pattern` attribute to define a regular expression that specifies the allowed input. For example, use `[A-Za-z]*` to allow only letters.
2. Define a shake animation using `@keyframes`. Set the `margin-left` property to move the input left and right.
3. Use the `:invalid` pseudo-class to apply the shake animation to the input.
4. Optionally, add a red box-shadow to the input to indicate the error.

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

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
