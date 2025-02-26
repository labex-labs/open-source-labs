# Área de arrastrar y soltar de archivos

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este componente permite la funcionalidad de arrastrar y soltar para un solo archivo. Para implementar este componente, siga estos pasos:

1. Cree una referencia llamada `dropRef` y asóciela con el envoltorio del componente.
2. Utilice el hook `useState()` para crear las variables `drag` y `filename`. Inicialízalas en `false` y `''` respectivamente.
3. Las variables `dragCounter` y `drag` se utilizan para determinar si se está arrastrando un archivo, mientras que `filename` se utiliza para almacenar el nombre del archivo soltado.
4. Cree los métodos `handleDrag`, `handleDragIn`, `handleDragOut` y `handleDrop` para manejar la funcionalidad de arrastrar y soltar. `handleDrag` evita que el navegador abra el archivo arrastrado, `handleDragIn` y `handleDragOut` manejan la entrada y salida del archivo arrastrado del componente, y `handleDrop` maneja la caída del archivo y lo pasa a `onDrop`.
5. Utilice el hook `useEffect()` para manejar cada uno de los eventos de arrastrar y soltar utilizando los métodos creados anteriormente.

Aquí está el CSS para el componente:

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

Aquí está el JSX para el componente:

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
      {filename && !drag ? (
        <div>{filename}</div>
      ) : (
        <div>Arrastre y suelte un archivo aquí!</div>
      )}
    </div>
  );
};
```

Para utilizar el componente, llame a `ReactDOM.createRoot(document.getElementById('root')).render(<FileDrop onDrop={console.log} />);`

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
