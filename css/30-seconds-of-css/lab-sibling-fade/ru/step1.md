# Прозрачность соседних элементов

В ВМ уже предоставлены файлы `index.html` и `style.css`.

Чтобы сделать соседние элементы элемента, на который наведён курсор, прозрачными:

1. Анимировать изменения `opacity` с использованием свойства `transition`.

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}
```

2. Изменить `opacity` для всех элементов, кроме того, на который наведён курсор, на `0.5` с использованием псевдо-классов `:hover` и `:not`.

```css
.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```

Вот пример HTML-кода:

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

Пожалуйста, нажмите кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
