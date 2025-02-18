# Hook useUnload de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual (VM). En general, solo necesitas agregar código a `script.js` y `style.css`.

El evento de ventana `beforeunload` se puede manejar utilizando los siguientes pasos:

1. Crea una referencia (ref) para la función de devolución de llamada (callback), `fn`, utilizando el hook `useRef()`.
2. Utiliza el hook `useEffect()` y `EventTarget.addEventListener()` para manejar el evento `'beforeunload'`, que se activa cuando el usuario está a punto de cerrar la ventana.
3. Utiliza `EventTarget.removeEventListener()` para realizar la limpieza después de que el componente se desmonte.

Aquí está el código:

```jsx
const useUnload = (fn) => {
  const callbackRef = React.useRef(fn);

  React.useEffect(() => {
    const callback = callbackRef.current;
    window.addEventListener("beforeunload", callback);
    return () => {
      window.removeEventListener("beforeunload", callback);
    };
  }, [callbackRef]);
};

const App = () => {
  useUnload((e) => {
    e.preventDefault();
    const exit = confirm("Are you sure you want to leave?");
    if (exit) window.close();
  });

  return <div>Try closing the window.</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
