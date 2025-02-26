# React хук useBodyScrollLock

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот фрагмент кода позволяет пользователям заблокировать прокрутку тела, когда открыто модальное окно. Вот, как это работает:

Во - первых, определена функция `useBodyScrollLock`, которая использует хук `useLayoutEffect` для блокировки прокрутки элемента `body`. Этот хук запускается только один раз при монтировании компонента, и он устанавливает значение `overflow` элемента `body` в `'hidden'`. Когда компонент демонтируется, восстанавливается исходное значение `overflow`.

```jsx
const useBodyScrollLock = () => {
  React.useLayoutEffect(() => {
    const originalStyle = window.getComputedStyle(document.body).overflow;
    document.body.style.overflow = "hidden";
    return () => (document.body.style.overflow = originalStyle);
  }, []);
};
```

Затем определен компонент `Modal`, который использует функцию `useBodyScrollLock`. Этот компонент отображает сообщение в коробке, которая центрирована на экране. Когда коробка нажимается, модальное окно закрывается и разблокируется прокрутка тела.

```jsx
const Modal = ({ onClose }) => {
  useBodyScrollLock();

  return (
    <div
      style={{
        zIndex: 100,
        background: "rgba(0,0,0,0.25)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
      onClick={onClose}
    >
      <p style={{ padding: 8, borderRadius: 8, background: "#fff" }}>
        Scroll заблокирован! <br /> Нажмите на меня, чтобы разблокировать
      </p>
    </div>
  );
};
```

Наконец, определен компонент `MyApp`, который отображает кнопку, при нажатии на которую открывается компонент `Modal`.

```jsx
const MyApp = () => {
  const [modalOpen, setModalOpen] = React.useState(false);

  return (
    <div
      style={{
        height: "400vh",
        textAlign: "center",
        paddingTop: 100,
        background: "linear-gradient(to bottom, #1fa2ff, #12d8fa, #a6ffcb)"
      }}
    >
      <button onClick={() => setModalOpen(true)}>Открыть модальное окно</button>
      {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб - сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб - страницу.
