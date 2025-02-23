# Настройка выделения текста

В ВМ уже предоставлены `index.html` и `style.css`.

Для изменения стиля выделенного текста используйте псевдо-селектор `::selection`. Вот пример фрагмента кода для выбора и стилизации текста внутри элемента абзаца:

```html
<p class="custom-text-selection">Select some of this text.</p>
```

```css
::selection {
  background: aquamarine;
  color: black;
}

.custom-text-selection::selection {
  background: deeppink;
  color: white;
}
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
