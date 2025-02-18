# Закрываемое уведомление (Closable Alert)

> Файлы `index.html` и `script.js` уже предоставлены в виртуальной машине (VM). В целом, вам нужно добавить код только в файлы `script.js` и `style.css`.

Рендерит компонент уведомления (alert) с пропсом `type`.

Компонент `Alert` принимает следующие пропсы:

- `isDefaultShown`: логическое значение (boolean), которое определяет, отображается ли уведомление изначально или нет (по умолчанию `false`)
- `timeout`: число, которое указывает продолжительность в миллисекундах до исчезания уведомления (по умолчанию `250`)
- `type`: строка, которая определяет тип уведомления (например, "warning", "error", "info")
- `message`: строка, содержащая сообщение, которое будет отображено в уведомлении

Компонент выполняет следующие действия:

- Использует хук `useState()` для создания переменных состояния `isShown` и `isLeaving` и изначально устанавливает их в `false`.
- Определяет переменную `timeoutId` для хранения экземпляра таймера, чтобы очистить его при размонтировании компонента.
- Использует хук `useEffect()` для обновления значения `isShown` на `true` и очистки интервала с помощью `timeoutId` при размонтировании компонента.
- Определяет функцию `closeAlert` для удаления компонента из DOM с помощью анимации исчезания и установки `isShown` в `false` с использованием `setTimeout()`.
- Рендерит компонент уведомления, если `isShown` равно `true`. Компонент имеет соответствующие стили на основе пропса `type` и исчезает, если `isLeaving` равно `true`.

Вот код:

```css
@keyframes leave {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.alert {
  padding: 0.75rem 0.5rem;
  margin-bottom: 0.5rem;
  text-align: left;
  padding-right: 40px;
  border-radius: 4px;
  font-size: 16px;
  position: relative;
}

.alert.warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.alert.leaving {
  animation: leave 0.5s forwards;
}

.alert.close {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0 0.75rem;
  color: #333;
  border: 0;
  height: 100%;
  cursor: pointer;
  background: none;
  font-weight: 600;
  font-size: 16px;
}

.alert.close::after {
  content: "x";
}
```

```jsx
const Alert = ({ isDefaultShown = false, timeout = 250, type, message }) => {
  const [isShown, setIsShown] = React.useState(isDefaultShown);
  const [isLeaving, setIsLeaving] = React.useState(false);

  let timeoutId = null;

  React.useEffect(() => {
    setIsShown(true);
    return () => {
      clearTimeout(timeoutId);
    };
  }, [isDefaultShown, timeout, timeoutId]);

  const closeAlert = () => {
    setIsLeaving(true);
    timeoutId = setTimeout(() => {
      setIsLeaving(false);
      setIsShown(false);
    }, timeout);
  };

  return (
    isShown && (
      <div
        className={`alert ${type} ${isLeaving ? "leaving" : ""}`}
        role="alert"
      >
        <button className="close" onClick={closeAlert} />
        {message}
      </div>
    )
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Alert type="info" message="This is info" />
);
```

Нажмите на кнопку 'Go Live' в правом нижнем углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб-страницу.
