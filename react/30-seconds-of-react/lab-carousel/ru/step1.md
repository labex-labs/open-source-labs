# Карусель

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот код отображает компонент карусели. Вот шаги, которые он выполняет:

1. Он использует хук `useState()`, чтобы создать переменную состояния `active` и инициализировать ее значением `0` (индекс первого элемента в карусели).
2. Он использует хук `useEffect()`, чтобы установить таймер с использованием `setTimeout()`. Когда таймер срабатывает, он обновляет значение `active` на индекс следующего элемента в карусели (с использованием оператора модуля, чтобы вернуться в начало, если необходимо). Он также очищает таймер, когда компонент демонтируется.
3. Он вычисляет `className` для каждого элемента карусели, проходя по ним и применяя соответствующий класс в зависимости от того, является ли элемент текущим активным или нет.
4. Он отображает элементы карусели с использованием `React.cloneElement()`, передавая любые дополнительные свойства с использованием `...rest`, и добавляя вычисленный `className` к каждому элементу.

CSS-стили определяют макет карусели и ее элементов. Контейнер карусели имеет `position: relative`, в то время как элементы по умолчанию имеют `position: absolute` и `visibility: hidden`. Когда элемент активен, он получает класс `visible`, который устанавливает его `visibility` в `visible`.

```css
.carousel {
  position: relative;
}

.carousel-item {
  position: absolute;
  visibility: hidden;
}

.carousel-item.visible {
  visibility: visible;
}
```

Вот полный код:

```jsx
const Carousel = ({ carouselItems, ...rest }) => {
  const [active, setActive] = React.useState(0);
  let scrollInterval = null;

  React.useEffect(() => {
    scrollInterval = setTimeout(() => {
      setActive((active + 1) % carouselItems.length);
    }, 2000);
    return () => clearTimeout(scrollInterval);
  });

  return (
    <div className="carousel">
      {carouselItems.map((item, index) => {
        const activeClass = active === index ? " visible" : "";
        return React.cloneElement(item, {
          ...rest,
          className: `carousel-item${activeClass}`
        });
      })}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <Carousel
    carouselItems={[
      <div>элемент карусели 1</div>,
      <div>элемент карусели 2</div>,
      <div>элемент карусели 3</div>
    ]}
  />
);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
