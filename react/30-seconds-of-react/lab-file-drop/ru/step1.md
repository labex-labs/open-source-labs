# Область для перетаскивания и вставки файлов

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавить код в `script.js` и `style.css`.

Этот компонент позволяет осуществлять функциональность перетаскивания и вставки одного файла. Чтобы реализовать этот компонент, следуйте шагам:

1. Создайте ссылку под названием `dropRef` и привяжите ее к обертке компонента.
2. Используйте хук `useState()` для создания переменных `drag` и `filename`. Инициализируйте их соответственно значениями `false` и `''`.
3. Переменные `dragCounter` и `drag` используются для определения, находится ли файл в процессе перетаскивания, в то время как `filename` используется для хранения имени перетаскиваемого файла.
4. Создайте методы `handleDrag`, `handleDragIn`, `handleDragOut` и `handleDrop` для обработки функциональности перетаскивания и вставки. `handleDrag` предотвращает открытие перетаскиваемого файла браузером, `handleDragIn` и `handleDragOut` обрабатывают вход и выход перетаскиваемого файла из компонента, а `handleDrop` обрабатывает dropping файла и передает его в `onDrop`.
5. Используйте хук `useEffect()` для обработки каждого события перетаскивания и вставки с использованием ранее созданных методов.

Вот CSS для компонента:

```css
.filedrop {
  min-height: 120px;
  border: 3px solid #d3d3d3;
  text-align: center;
  font-size: 24px;
  padding: 32px;
  border-radius: 4px;
}

.filedrop.drag {
  border: 3px dashed #1e90ff;
}

.filedrop.ready {
  border: 3px solid #32cd32;
}
```

Вот JSX для компонента:

```jsx
const FileDrop = ({ onDrop }) => {
  const [drag, setDrag] = React.useState(false);
  const [filename, setFilename] = React.useState("");
  const dropRef = React.useRef(null);
  let dragCounter = 0;

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDragIn = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter++;
    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
  };

  const handleDragOut = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter--;
    if (dragCounter === 0) setDrag(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDrag(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onDrop(e.dataTransfer.files[0]);
      setFilename(e.dataTransfer.files[0].name);
      e.dataTransfer.clearData();
      dragCounter = 0;
    }
  };

  React.useEffect(() => {
    const div = dropRef.current;
    div.addEventListener("dragenter", handleDragIn);
    div.addEventListener("dragleave", handleDragOut);
    div.addEventListener("dragover", handleDrag);
    div.addEventListener("drop", handleDrop);
    return () => {
      div.removeEventListener("dragenter", handleDragIn);
      div.removeEventListener("dragleave", handleDragOut);
      div.removeEventListener("dragover", handleDrag);
      div.removeEventListener("drop", handleDrop);
    };
  }, []);

  return (
    <div
      ref={dropRef}
      className={
        drag ? "filedrop drag" : filename ? "filedrop ready" : "filedrop"
      }
    >
      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
    </div>
  );
};
```

Для использования компонента вызовите `ReactDOM.createRoot(document.getElementById('root')).render(<FileDrop onDrop={console.log} />);`

Пожалуйста, нажмите на кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
