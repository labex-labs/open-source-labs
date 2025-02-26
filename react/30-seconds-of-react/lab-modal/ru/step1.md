# Модальное окно

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот код отображает компонент Modal, который можно контролировать с помощью событий. Чтобы использовать компонент, вы можете импортировать `Modal` один раз, а затем отобразить его, передав логическое значение в атрибут `isVisible`.

Компонент Modal имеет следующие характеристики:

- Он определяет функцию `keydownHandler`, которая обрабатывает все события клавиатуры и вызывает `onClose`, когда нажимается клавиша `Esc`.
- Он использует хук `useEffect()` для добавления или удаления слушателя события `keydown` к `Document`, вызывая `keydownHandler` для каждого события.
- Он добавляет стилизованный элемент `<span>`, который действует как кнопка закрытия, вызывая `onClose` при нажатии.
- Он использует пропс `isVisible`, переданный из родительского компонента, чтобы определить, должно ли модальное окно быть отображено или нет.
- Он включает в себя CSS-файл, который стилизует компонент Modal.

```jsx
const Modal = ({ isVisible = false, title, content, footer, onClose }) => {
  const keydownHandler = ({ key }) => {
    switch (key) {
      case "Escape":
        onClose();
        break;
      default:
    }
  };

  React.useEffect(() => {
    document.addEventListener("keydown", keydownHandler);
    return () => document.removeEventListener("keydown", keydownHandler);
  });

  return !isVisible ? null : (
    <div className="modal" onClick={onClose}>
      <div className="modal-dialog" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h3 className="modal-title">{title}</h3>
          <span className="modal-close" onClick={onClose}>
            &times;
          </span>
        </div>
        <div className="modal-body">
          <div className="modal-content">{content}</div>
        </div>
        {footer && <div className="modal-footer">{footer}</div>}
      </div>
    </div>
  );
};
```

```css
.modal {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.25);
  animation-name: appear;
  animation-duration: 300ms;
}

.modal-dialog {
  width: 100%;
  max-width: 550px;
  background: white;
  position: relative;
  margin: 0 20px;
  max-height: calc(100vh - 40px);
  text-align: left;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  box-shadow:
    0 4px 8px 0 rgba(0, 0, 0, 0.2),
    0 6px 20px 0 rgba(0, 0, 0, 0.19);
  -webkit-animation-name: animatetop;
  -webkit-animation-duration: 0.4s;
  animation-name: slide-in;
  animation-duration: 0.5s;
}

.modal-header,
.modal-footer {
  display: flex;
  align-items: center;
  padding: 1rem;
}

.modal-header {
  border-bottom: 1px solid #dbdbdb;
  justify-content: space-between;
}

.modal-footer {
  border-top: 1px solid #dbdbdb;
  justify-content: flex-end;
}

.modal-close {
  cursor: pointer;
  padding: 1rem;
  margin: -1rem -1rem -1rem auto;
}

.modal-body {
  overflow: auto;
}

.modal-content {
  padding: 1rem;
}

@keyframes appear {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slide-in {
  from {
    transform: translateY(-150px);
  }
  to {
    transform: translateY(0);
  }
}
```

```jsx
const App = () => {
  const [isModal, setModal] = React.useState(false);
  return (
    <>
      <button onClick={() => setModal(true)}>Click Here</button>
      <Modal
        isVisible={isModal}
        title="Modal Title"
        content={<p>Add your content here</p>}
        footer={<button>Cancel</button>}
        onClose={() => setModal(false)}
      />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
