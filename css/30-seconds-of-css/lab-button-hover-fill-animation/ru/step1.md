# Анимация заполнения кнопки

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания анимации заполнения при наведении можно задать свойства `color` и `background` и применить соответствующий `transition`, чтобы анимировать изменения. Для запуска анимации при наведении используйте псевдо-класс `:hover`, чтобы изменить свойства `background` и `color` элемента. Вот пример фрагмента кода:

```html
<button class="animated-fill-button">Submit</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем можно обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
