# Hook useInterval de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para implementar `setInterval()` de manera declarativa, se puede crear un hook personalizado que tome una `callback` y un `delay`. El primer paso es utilizar el hook `useRef()` para crear una `ref` para la función de devolución de llamada. Luego, utilizar un hook `useEffect()` para recordar la última `callback` cada vez que cambie. Finalmente, utilizar un hook `useEffect()` dependiente de `delay` para configurar el intervalo y limpiar.

A continuación, se muestra un fragmento de código de ejemplo para el hook personalizado:

```jsx
const useInterval = (callback, delay) => {
  const savedCallback = React.useRef();

  React.useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  React.useEffect(() => {
    const tick = () => {
      savedCallback.current();
    };
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
};
```

Luego, se puede utilizar este hook personalizado en sus componentes. Por ejemplo, para crear un temporizador que se actualice cada segundo:

```jsx
const Timer = (props) => {
  const [seconds, setSeconds] = React.useState(0);

  useInterval(() => {
    setSeconds(seconds + 1);
  }, 1000);

  return <p>{seconds}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Timer />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
