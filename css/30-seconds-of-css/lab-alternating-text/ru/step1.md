# Альтернативный текст

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания анимации сменяющегося текста следуйте шагам:

1. Создайте элемент `<span>` с классом "alternating" и идентификатором "alternating-text", чтобы хранить текст, который будет меняться:

```html
<p>I love coding in <span class="alternating" id="alternating-text"></span>.</p>
```

2. В CSS определите анимацию под названием `alternating-text`, которая будет скрывать элемент `<span>`, установив `display: none`:

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

3. В JavaScript определите массив различных слов, которые будут меняться, и используйте первое слово для инициализации содержимого элемента `<span>`:

```js
const texts = ["Java", "Python", "C", "C++", "C#", "Javascript"];
const element = document.getElementById("alternating-text");

let i = 0;
element.innerHTML = texts[0];
```

4. Используйте `EventTarget.addEventListener()` для определения слушателя событий для события `'animationiteration'`. Это вызовет обработчик событий каждый раз, когда завершается итерация анимации. В обработчике событий используйте `Element.innerHTML`, чтобы отобразить следующий элемент в массиве `texts` в качестве содержимого элемента `<span>`:

```js
const listener = (e) => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.addEventListener("animationiteration", listener, false);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
