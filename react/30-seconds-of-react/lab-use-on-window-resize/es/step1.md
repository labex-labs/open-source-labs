# Hook useOnWindowResize de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este código ejecuta una función de devolución de llamada cada vez que se redimensiona la ventana. Para implementarlo, debes seguir estos pasos:

1. Crea una variable llamada `listener` utilizando el Hook `useRef()`. Esta variable almacenará la referencia al oyente.

2. Utiliza el Hook `useEffect()` y `EventTarget.addEventListener()` para escuchar el evento `'resize'` del objeto global `Window`. Cuando se active el evento, llama a la función `callback`.

3. Limpia eliminando cualquier oyente existente con `EventTarget.removeEventListener()` cuando el componente se desmonte.

Aquí está el código:

```jsx
const useOnWindowResize = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("resize", listener.current);
    }
    listener.current = callback;
    window.addEventListener("resize", callback);
    return () => {
      window.removeEventListener("resize", callback);
    };
  }, [callback]);
};

const App = () => {
  useOnWindowResize(() =>
    console.log(
      `Tamaño de la ventana: (${window.innerWidth}, ${window.innerHeight})`
    )
  );
  return <p>Redimensiona la ventana y revisa la consola.</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
