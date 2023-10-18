# Typewriter Effect

`index.html` and `style.css` have already been provided in the VM.

To create a typewriter effect animation, follow these steps:

1. Define two animations, `typing` and `blink`. `typing` animates the characters, and `blink` animates the caret.
2. Use the `::after` pseudo-element to add the caret to the container element.
3. Use JavaScript to set the text for the inner element and set the `--characters` variable, which contains the character count. This variable is used to animate the text.
4. Use `white-space: nowrap` and `overflow: hidden` to make content invisible as necessary.

Here's the HTML code:

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

And here's the CSS code:

```css
.typewriter-effect {
  display: flex;
  justify-content: center;
  font-family: monospace;
}

.typewriter-effect > .text {
  max-width: 0;
  animation: typing 3s steps(var(--characters)) infinite;
  white-space: nowrap;
  overflow: hidden;
}

.typewriter-effect::after {
  content: " |";
  animation: blink 1s infinite;
  animation-timing-function: step-end;
}

@keyframes typing {
  75%,
  100% {
    max-width: calc(var(--characters) * 1ch);
  }
}

@keyframes blink {
  0%,
  75%,
  100% {
    opacity: 1;
  }
  25% {
    opacity: 0;
  }
}
```

And finally, here's the JavaScript code:

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the **Web 8080** Tab to preview the web page.
