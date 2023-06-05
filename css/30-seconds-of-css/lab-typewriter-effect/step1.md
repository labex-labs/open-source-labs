# Typewriter Effect

This code block creates a typewriter effect animation by defining two animations: `typing` to animate the characters and `blink` to animate the caret. It uses the `::after` pseudo-element to add the caret to the container element. The text for the inner element is set using JavaScript and the `--characters` variable containing the character count. This variable is used to animate the text. Finally, `white-space: nowrap` and `overflow: hidden` are used to make content invisible as necessary.

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

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
  75%, 100% {
    max-width: calc(var(--characters) * 1ch);
  }
}

@keyframes blink {
  0%, 75%, 100% {
    opacity: 1;
  }
  25% {
    opacity: 0;
  }
}
```

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```