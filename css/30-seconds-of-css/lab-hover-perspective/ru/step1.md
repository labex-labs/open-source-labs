# Перспективное преобразование при наведении курсора

В ВМ уже предоставлены `index.html` и `style.css`.

Для создания перспективного преобразования с анимацией при наведении курсора на элемент:

1. Используйте свойство `transform` с функциями `perspective()` и `rotateY()` для применения перспективы к элементу. Например, чтобы создать левую перспективу, используйте `transform: perspective(1500px) rotateY(15deg);`. Чтобы создать правую перспективу, используйте `transform: perspective(1500px) rotateY(-15deg);`.

2. Используйте свойство `transition` для анимации свойства `transform` при наведении курсора на элемент. Например, `transition: transform 1s ease 0s;`.

3. Чтобы отразить эффект перспективы слева направо, измените значение `rotateY()` на отрицательное при правой перспективе. Например, используйте `transform: perspective(1500px) rotateY(-15deg);`.

Пример HTML:

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

Пример CSS:

```css
.image-card {
  display: inline-block;
  box-sizing: border-box;
  margin: 1rem;
  width: 240px;
  height: 320px;
  padding: 8px;
  border-radius: 1rem;
  background: url("https://picsum.photos/id/1049/240/320");
  box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
}

.perspective-left {
  transform: perspective(1500px) rotateY(15deg);
  transition: transform 1s ease 0s;
}

.perspective-left:hover {
  transform: perspective(3000px) rotateY(5deg);
}

.perspective-right {
  transform: perspective(1500px) rotateY(-15deg);
  transition: transform 1s ease 0s;
}

.perspective-right:hover {
  transform: perspective(3000px) rotateY(-5deg);
}
```

Пожалуйста, нажмите на кнопку "Go Live" в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
