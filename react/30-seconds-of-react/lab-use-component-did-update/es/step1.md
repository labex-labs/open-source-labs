# React useComponentDidUpdate Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este código proporciona un hook personalizado llamado `useComponentDidUpdate` que ejecuta una función `callback` proporcionada cada vez que un componente se actualiza. Estos son los pasos que sigue el hook:

1. Crea una variable `mounted` usando el hook `useRef()`. Esta variable rastrea si el componente ha sido montado o no.
2. Utiliza el hook `useEffect()` para establecer el valor de `mounted` en `true` la primera vez que se ejecuta el hook.
3. En ejecuciones posteriores del hook, ejecuta la función `callback` proporcionada solo si el componente ya ha sido montado.
4. Si se proporciona un segundo argumento `condition`, el hook solo se ejecutará si cualquiera de sus dependencias cambia.
5. Este hook se comporta como el método de ciclo de vida `componentDidUpdate()` de los componentes de clase.

Aquí está el código:

```jsx
const useComponentDidUpdate = (callback, condition) => {
  const isMounted = React.useRef(false);
  React.useEffect(() => {
    if (isMounted.current) {
      callback();
    } else {
      isMounted.current = true;
    }
  }, condition);
};

const App = () => {
  const [value, setValue] = React.useState(0);
  const [otherValue, setOtherValue] = React.useState(1);

  useComponentDidUpdate(() => {
    console.log(`Current value is ${value}.`);
  }, [value]);

  return (
    <>
      <p>
        Value: {value}, other value: {otherValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment value</button>
      <button onClick={() => setOtherValue(otherValue + 1)}>
        Increment other value
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
