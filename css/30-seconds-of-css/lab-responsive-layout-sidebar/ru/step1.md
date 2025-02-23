# Адаптивный макет с боковой панелью

В ВМ уже предоставлены файлы `index.html` и `style.css`.

Для создания адаптивного макета с областью содержимого и боковой панелью используйте `display: grid` для родительского контейнера, `minmax()` для второй колонки (боковой панели), чтобы она занимала от `150px` до `20%`, и `1fr` для первой колонки (основного содержимого), чтобы она занимала оставшееся пространство. Вот пример кода HTML и CSS:

```html
<div class="container">
  <main>This element is 1fr large.</main>
  <aside>Min: 150px / Max: 20%</aside>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 20%);
  height: 100px;
}

main,
aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #d4f2c4;
}

aside {
  background: #81cfd9;
}
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
