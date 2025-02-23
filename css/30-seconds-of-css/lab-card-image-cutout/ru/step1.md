# Карточка с вырезанной картинкой

В ВМ уже предоставлены `index.html` и `style.css`.

Чтобы создать карточку с вырезанной картинкой, следуйте шагам:

1. Добавьте цветной фон к элементу `.container` с использованием свойства `background`.
2. Создайте элемент `.card` и добавьте внутри него элемент `figure` с нужной картинкой и любым другим содержимым.
3. Используйте псевдо-элемент `::before` для добавления `рамки` вокруг элемента `figure`. Установите цвет рамки так, чтобы он совпадал с цветом `фона` элемента `.container`, чтобы создать иллюзию вырезки в `.card`.

Вот пример HTML-кода для карточки:

```html
<div class="container">
  <div class="card">
    <figure>
      <img alt="" src="https://picsum.photos/id/447/400/400" />
    </figure>
    <p class="content">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
</div>
```

И вот соответствующий CSS-код:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 96px 24px 48px;
  background: #f3f1fe;
}

.card {
  width: 350px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.card figure {
  width: 120px;
  height: 120px;
  margin-top: -60px;
  border-radius: 50%;
  position: relative;
}

.card figure::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  border-radius: inherit;
  border: 1rem solid #f3f1fe;
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
}

.card figure img {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  object-fit: cover;
}

.card.content {
  margin: 2rem;
  text-align: center;
  line-height: 1.5;
  color: #101010;
}
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
