# Эффект машинного пишущего

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать анимацию с эффектом машинного пишущего, следуйте шагам:

1. Определите две анимации: `typing` и `blink`. `typing` анимирует символы, а `blink` анимирует курсор.
2. Используйте псевдо-элемент `::after`, чтобы добавить курсор к элементу-контейнеру.
3. Используйте JavaScript для установки текста для внутреннего элемента и установки переменной `--characters`, которая содержит количество символов. Эта переменная используется для анимации текста.
4. Используйте `white-space: nowrap` и `overflow: hidden`, чтобы скрыть контент при необходимости.

Вот HTML-код:

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

Вот CSS-код:

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

Наконец, вот JavaScript-код:

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
