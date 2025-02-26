# Hook useEffectOnce de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

El código siguiente implementa una función `useEffectOnce(callback, when)` que ejecuta una `callback` solo una vez cuando una condición `when` se vuelve verdadera.

Para implementar esta función:

- Cree una variable `hasRunOnce` usando el hook `useRef()` para controlar el estado de ejecución del efecto.
- Utilice el hook `useEffect()` que solo se ejecuta cuando cambia la condición `when`.
- Dentro del hook `useEffect()`, verifique si `when` es `true` y el efecto no se ha ejecutado antes. Si ambos son `true`, ejecute `callback` y establezca `hasRunOnce` en `true`.

```jsx
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

A continuación, se muestra un ejemplo de uso de `useEffectOnce()`:

```jsx
const App = () => {
  const [clicked, setClicked] = React.useState(false);
  useEffectOnce(() => {
    console.log("montado");
  }, clicked);
  return <button onClick={() => setClicked(true)}>Ház clic en mí</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

En el ejemplo, `useEffectOnce()` se utiliza para registrar "montado" en la consola cuando se hace clic en el botón por primera vez. El hook `useEffectOnce()` se pasa dos argumentos: la `callback` a ejecutar y la condición `when` a verificar. La condición `when` se establece en el estado `clicked`, por lo que la `callback` solo se ejecuta cuando `clicked` es `true` por primera vez.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
