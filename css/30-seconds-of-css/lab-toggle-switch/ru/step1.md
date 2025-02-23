# Переключатель

В ВМ уже предоставлены `index.html` и `style.css`.

Вот более краткая и ясная версия содержания:

Для создания переключателя с использованием только CSS следуйте этим шагам:

1. Свяжите `<label>` с элементом `<input>` checkbox с использованием атрибута `for`.
2. Используйте псевдо-элемент `::after` элемента `<label>` для создания круглой ручки для переключателя.
3. Используйте псевдо-класс селектор `:checked` для изменения положения ручки с использованием `transform: translateX(20px)` и `background-color` переключателя.
4. Визуально скрыть элемент `<input>` с использованием `position: absolute` и `left: -9999px`.

Вот HTML-код:

```html
<input type="checkbox" id="toggle" class="offscreen" />
<label for="toggle" class="switch"></label>
```

Вот CSS-код:

```css
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  transition: all 0.3s;
}

.switch::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 18px;
  background-color: white;
  top: 1px;
  left: 1px;
  transition: all 0.3s;
}

input[type="checkbox"]:checked + .switch::after {
  transform: translateX(20px);
}

input[type="checkbox"]:checked + .switch {
  background-color: #7983ff;
}

.offscreen {
  position: absolute;
  left: -9999px;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
