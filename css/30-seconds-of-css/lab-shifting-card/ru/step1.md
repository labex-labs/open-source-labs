# Сдвигающийся карточный элемент

В ВМ уже предоставлены файлы `index.html` и `style.css`.

Чтобы создать карточный элемент, который будет сдвигаться при наведении курсора, следуйте шагам ниже:

1. Задайте подходящую `perspective` для элемента `.container`, чтобы обеспечить эффект сдвига.
2. Добавьте `transition` для свойства `transform` элемента `.card`.
3. Используйте `Document.querySelector()`, чтобы выбрать элемент `.card` и добавьте слушатели событий для событий `mousemove` и `mouseout`.
4. Используйте `Element.getBoundingClientRect()`, чтобы получить `x`, `y`, `width` и `height` элемента `.card`.
5. Вычислите относительное расстояние в виде значения между `-1` и `1` для осей `x` и `y` и примените его через свойство `transform`.

Вот пример кода HTML и CSS для карточки:

```html
<div class="container">
  <div class="shifting-card">
    <div class="content">
      <h3>Card</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti
        repellat, consequuntur doloribus voluptate esse iure?
      </p>
    </div>
  </div>
</div>
```

```css
.container {
  display: flex;
  padding: 24px;
  justify-content: center;
  align-items: center;
  background: #f3f1fe;
  perspective: 1000px;
}

.shifting-card {
  width: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  margin: 0.5rem;
  transition: transform 0.2s ease-out;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.shifting-card.content {
  text-align: center;
  margin: 2rem;
  line-height: 1.5;
  color: #101010;
}
```

Вот код JavaScript для добавления эффекта наведения:

```js
const card = document.querySelector(".shifting-card");
const { x, y, width, height } = card.getBoundingClientRect();
const cx = x + width / 2;
const cy = y + height / 2;

const handleMove = (e) => {
  const { pageX, pageY } = e;
  const dx = (cx - pageX) / (width / 2);
  const dy = (cy - pageY) / (height / 2);
  e.target.style.transform = `rotateX(${10 * dy * -1}deg) rotateY(${
    10 * dx
  }deg)`;
};

const handleOut = (e) => {
  e.target.style.transform = "initial";
};

card.addEventListener("mousemove", handleMove);
card.addEventListener("mouseout", handleOut);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
