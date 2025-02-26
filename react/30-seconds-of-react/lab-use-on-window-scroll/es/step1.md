# Hook useOnWindowScroll de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función ejecuta una función de devolución de llamada cada vez que se desliza la ventana. Para implementarla:

1. Use el hook `useRef()` para crear una variable de referencia, `listener`.
2. Use el hook `useEffect()` y `EventTarget.addEventListener()` para escuchar el evento `'scroll'` del objeto `Window`, y asignar la referencia del oyente a `listener.current`.
3. Use `EventTarget.removeEventListener()` para eliminar cualquier oyente existente cuando el componente se desmonte.

Aquí está el código:

```jsx
const useOnWindowScroll = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("scroll", listener.current);
    }
    listener.current = () => {
      callback(window.pageYOffset);
    };
    window.addEventListener("scroll", listener.current);
    return () => {
      window.removeEventListener("scroll", listener.current);
    };
  }, [callback]);
};
```

Para probar la función, se puede usar en un componente de la siguiente manera:

```jsx
const App = () => {
  useOnWindowScroll((scrollY) => console.log(`scroll Y: ${scrollY}`));
  return <p style={{ height: "300vh" }}>Scroll and check the console</p>;
};

ReactDOM.render(<App />, document.getElementById("root"));
```

Esto registrará la posición de desplazamiento vertical de la ventana cada vez que se deslice.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
