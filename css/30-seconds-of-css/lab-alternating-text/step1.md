# Alternating Text

`index.html` and `style.css` have already been provided in the VM.

To create an alternating text animation, follow these steps:

1. Create a `<span>` element with a class of "alternating" and an `id` of "alternating-text" to hold the text that will be alternated:
```html
<p>I love coding in <span class="alternating" id="alternating-text"></span>.</p>
```

2. In the CSS, define an animation called `alternating-text` that will make the `<span>` element disappear by setting `display: none`:
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

3. In JavaScript, define an array of the different words that will be alternated and use the first word to initialize the content of the `<span>` element:
```js
const texts = ['Java', 'Python', 'C', 'C++', 'C#', 'Javascript'];
const element = document.getElementById('alternating-text');

let i = 0;
element.innerHTML = texts[0];
```

4. Use `EventTarget.addEventListener()` to define an event listener for the `'animationiteration'` event. This will run the event handler whenever an iteration of the animation is completed. In the event handler, use `Element.innerHTML` to display the next element in the `texts` array as the content of the `<span>` element:
```js
const listener = e => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.addEventListener('animationiteration', listener, false);
```

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
