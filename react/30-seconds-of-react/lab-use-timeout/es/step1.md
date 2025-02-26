# Hook useTimeout de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para implementar `setTimeout()` de manera declarativa, cree un hook personalizado que tome una `callback` y un `delay`. Utilice el hook `useRef()` para crear una `ref` para la función de devolución de llamada y el hook `useEffect()` para recordar la última función de devolución de llamada. Luego, utilice el hook `useEffect()` para configurar el temporizador y limpiarlo.

A continuación, se muestra un fragmento de código de ejemplo que demuestra este enfoque:

```jsx
const useTimeout = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setTimeout(tick, delay);
      return () => clearTimeout(id);
    }
  }, [delay]);
};

const OneSecondTimer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useTimeout(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<OneSecondTimer />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
