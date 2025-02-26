# Вращающийся загрузчик

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

**Отображает компонент вращающегося загрузчика.**

Чтобы отобразить компонент вращающегося загрузчика, следуйте шагам:

1. Отобразите элемент SVG, размеры которого определяются пропсом `size`.
2. Используйте CSS для создания анимации SVG, создавая вращающуюся анимацию. В частности, добавьте класс `.loader` к SVG и задайте свойство `animation` как `rotate 2s linear infinite`. Также определите ключевые кадры `rotate` с свойством `transform`, которое вращает SVG на 360 градусов.
3. Добавьте элемент `circle` в SVG, который представляет вращающийся круг. Чтобы анимировать круг, добавьте селектор `.loader circle` и задайте свойство `animation` как `dash 1.5s ease-in-out infinite`. Также определите ключевые кадры `dash` с свойствами `stroke-dasharray` и `stroke-dashoffset`, которые создают пунктирную линию, которая движется по кругу.
4. Наконец, создайте компонент `Loader`, который отображает SVG с пропсом `size`, переданным в качестве атрибутов ширины и высоты.

```css
.loader {
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}

.loader circle {
  animation: dash 1.5s ease-in-out infinite;
}

@keyframes dash {
  0% {
    stroke-dasharray: 1, 150;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -35;
  }
  100% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -124;
  }
}
```

```jsx
const Loader = ({ size }) => {
  return (
    <svg
      className="loader"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
    </svg>
  );
};
```

Чтобы использовать компонент `Loader` с размером 24, вызовите `ReactDOM.createRoot(document.getElementById('root')).render(<Loader size={24} />);`.

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
