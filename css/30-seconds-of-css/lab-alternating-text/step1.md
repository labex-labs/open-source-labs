# Alternating Text

To create an alternating text animation:

1. Add a `<span>` for the text that will be alternated.
2. Define an animation called `alternating-text` that hides the `<span>` by setting `display: none`.
3. In JavaScript, define an array of words to be alternated and use the first word to initialize the `<span>`.
4. Add an event listener to the `'animationiteration'` event using `EventTarget.addEventListener()`. This will run the `listener()` function whenever an iteration of the animation is completed.
5. In the `listener()` function, update the content of the `<span>` to the next word in the array using `Element.innerHTML`.

```html
<p>I love coding in <span class="alternating" id="alternating-text"></span>.</p>
```

```css
.alternating {
  animation-name: alternating-text;
  animation-duration: 3s;
  animation-iteration-count: infinite;
  animation-timing-function: ease;
}

@keyframes alternating-text {
  90% {
    display: none;
  }
}
```

```js
const texts = ["Java", "Python", "C", "C++", "C#", "Javascript"];
const element = document.getElementById("alternating-text");

let i = 0;
const listener = (e) => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.innerHTML = texts[0];
element.addEventListener("animationiteration", listener, false);
```