# Полоса прогресса прокрутки

`index.html` и `style.css` уже предоставлены в виртуальной машине (VM).

Для создания полосы прогресса, которая показывает процент прокрутки веб - страницы, следуйте этим шагам:

1. Добавьте элемент `div` с `id` "scroll-progress" в HTML - код.
2. В CSS - коде установите `position` элемента в `fixed`, `top` в `0`, `width` в `0%`, `height` в `4px` и цвет `background` в `#7983ff`.
3. Установите значение `z - index` большим числом, чтобы убедиться, что полоса прогресса находится вверху страницы и над любым контентом.
4. В JavaScript - коде выберите элемент `scroll - progress` с помощью метода `document.getElementById()`.
5. Вычислите высоту веб - страницы по формуле `document.documentElement.scrollHeight - document.documentElement.clientHeight`.
6. Добавьте слушатель события к объекту `window`, который отслеживает событие `scroll`.
7. В функции слушателя события вычислите процент прокрутки документа по формуле `(scrollTop / height) * 100`.
8. Установите `width` элемента `scroll - progress` равным проценту прокрутки с помощью свойства `style`.

Вот код:

```html
<div id="scroll-progress"></div>
```

```css
#scroll-progress {
  position: fixed;
  top: 0;
  width: 0%;
  height: 4px;
  background: #7983ff;
  z-index: 10000;
}
```

```js
const scrollProgress = document.getElementById("scroll-progress");
const height =
  document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener("scroll", () => {
  const scrollTop =
    document.body.scrollTop || document.documentElement.scrollTop;
  scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
});
```

Нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб - сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб - страницу.
