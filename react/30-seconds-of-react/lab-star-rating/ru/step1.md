# Оценка звезд

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Создайте компонент `Star`, который отображает каждую отдельную звезду с соответствующим внешним видом в зависимости от состояния родительского компонента. Затем определите компонент `StarRating`, который использует хук `useState()` для определения переменных состояния `rating` и `selection` с соответствующими начальными значениями.

В `StarRating` создайте метод с именем `hoverOver`, который обновляет `selection` в соответствии с предоставленным `event`. Если `event` не предоставлен или он равен `null`, сбросьте `selection` до `0`. Используйте атрибут `.data-star-id` целевого элемента события, чтобы определить значение `selection`.

Далее создайте массив из 5 элементов с использованием `Array.from()` и создайте отдельные компоненты `<Star>` с использованием `Array.prototype.map()`. Обработайте события `onMouseOver` и `onMouseLeave` оборачивающего элемента с использованием `hoverOver`. Обработайте событие `onClick` с использованием `setRating`.

```css
.star {
  color: #ff9933;
  cursor: pointer;
}
```

```jsx
const Star = ({ marked, starId }) => {
  return (
    <span data-star-id={starId} className="star" role="button">
      {marked ? "\u2605" : "\u2606"}
    </span>
  );
};

const StarRating = ({ value }) => {
  const [rating, setRating] = React.useState(parseInt(value) || 0);
  const [selection, setSelection] = React.useState(0);

  const hoverOver = (event) => {
    let val = 0;
    if (event && event.target && event.target.getAttribute("data-star-id"))
      val = event.target.getAttribute("data-star-id");
    setSelection(val);
  };

  return (
    <div
      onMouseLeave={() => hoverOver(null)}
      onMouseOver={hoverOver}
      onClick={(e) =>
        setRating(e.target.getAttribute("data-star-id") || rating)
      }
    >
      {Array.from({ length: 5 }, (v, i) => (
        <Star
          starId={i + 1}
          key={`star_${i + 1}`}
          marked={selection ? selection >= i + 1 : rating >= i + 1}
        />
      ))}
    </div>
  );
};
```

Наконец, отобразите компонент `StarRating` с начальным значением `2`, вызвав `ReactDOM.createRoot(document.getElementById('root')).render(<StarRating value={2} />);`.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
