# Макет из трех плиток

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания макета из трех плиток используйте `display: inline-block` вместо `float`, `flex` или `grid`. Используйте `width` в сочетании с `calc`, чтобы равномерно разделить ширину контейнера на три колонки. Чтобы избежать появления пробелов между элементами, установите `font-size` равным `0` для `.tiles`, а для элементов `<h2>` — `20px`, чтобы отобразить текст. Обратите внимание, что использование `font-size: 0` для устранения пробелов между блоками может привести к побочным эффектам, если вы используете относительные единицы (например, `em`).

```html
<div class="tiles">
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
</div>
```

```css
.tiles {
  width: 600px;
  font-size: 0;
  margin: 0 auto;
}

.tile {
  width: calc(600px / 3);
  display: inline-block;
}

.tile h2 {
  font-size: 20px;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
