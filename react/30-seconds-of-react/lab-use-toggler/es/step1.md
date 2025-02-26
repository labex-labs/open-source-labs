# React useToggler Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para crear una variable de estado booleana que se puede alternar entre sus dos estados, siga estos pasos:

1. Utilice el hook `useState()` para crear la variable de estado `value` y su setter.
2. Cree una función que alterna el valor de la variable de estado `value` y mémoízela, utilizando el hook `useCallback()`.
3. Devuelva la variable de estado `value` y la función de alternancia mémoizada.

A continuación, se muestra una implementación de ejemplo:

```jsx
const useToggler = (initialState) => {
  const [value, setValue] = React.useState(initialState);

  const toggleValue = React.useCallback(() => setValue((prev) => !prev), []);

  return [value, toggleValue];
};
```

Luego, puede usar este hook en sus componentes, de la siguiente manera:

```jsx
const Switch = () => {
  const [val, toggleVal] = useToggler(false);
  return <button onClick={toggleVal}>{val ? "ON" : "OFF"}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Switch />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
