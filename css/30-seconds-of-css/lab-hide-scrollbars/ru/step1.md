# Скрыть полосы прокрутки

В ВМ уже предоставлены `index.html` и `style.css`.

Для того, чтобы элемент был прокручиваемым, при этом скрывая полосы прокрутки, следуйте шагам:

- Используйте `overflow: auto`, чтобы включить прокрутку на элементе.
- Используйте `scrollbar-width: none`, чтобы скрыть полосы прокрутки в Firefox.
- Используйте `display: none` на псевдо-элементе `::-webkit-scrollbar`, чтобы скрыть полосы прокрутки в браузерах на основе WebKit (например, Chrome, Edge и Safari).

Вот пример реализации:

```html
<div class="scrollable">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
.scrollable {
  width: 200px;
  height: 100px;
  overflow: auto;
  scrollbar-width: none;
}

/* Hide scrollbars on WebKit browsers */
.scrollable::-webkit-scrollbar {
  display: none;
}
```

Пожалуйста, нажмите на кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
