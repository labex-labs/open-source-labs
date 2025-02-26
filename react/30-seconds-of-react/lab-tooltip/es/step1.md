# Información emergente

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Aquí está una versión más clara, concisa y coherente del contenido:

---

Este código crea un componente de información emergente. Para usarlo, siga estos pasos:

1. Utilice el hook `useState()` para crear la variable `show` y establezca su valor en `false`.
2. Renderice un elemento de contenedor que contenga el elemento de información emergente y los `children` pasados al componente.
3. Maneje los eventos `onMouseEnter` y `onMouseLeave` alternando la `className` de la información emergente, que está controlada por la variable `show`.

Aquí está el código para el componente de información emergente:

```css
.tooltip-container {
  position: relative;
}

.tooltip-box {
  position: absolute;
  top: calc(100% + 5px);
  display: none;
  padding: 5px;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
}

.tooltip-box.visible {
  display: block;
}

.tooltip-arrow {
  position: absolute;
  top: -10px;
  left: 50%;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgba(0, 0, 0, 0.7) transparent;
}
```

```jsx
const Tooltip = ({ children, text, ...rest }) => {
  const [show, setShow] = React.useState(false);

  return (
    <div className="tooltip-container">
      <div className={show ? "tooltip-box visible" : "tooltip-box"}>
        {text}
        <span className="tooltip-arrow" />
      </div>
      <div
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        {...rest}
      >
        {children}
      </div>
    </div>
  );
};
```

Para usar el componente de información emergente, llame a `ReactDOM.createRoot()` con el siguiente código:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tooltip text="Información emergente simple">
    <button>¡Pásale el cursor!</button>
  </Tooltip>
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
