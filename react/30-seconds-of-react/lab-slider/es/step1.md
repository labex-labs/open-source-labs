# Entrada de rango no controlada

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para crear un deslizador en React, use el componente `Slider` y pase las propiedades `min`, `max`, `defaultValue` y `onValueChange`.

En el componente `Slider`, establezca el `type` del elemento `<input>` en `"range"` para crear un deslizador. Utilice la prop `defaultValue` heredada del padre como el valor inicial del campo de entrada no controlado. Utilice el evento `onChange` para activar la devolución de llamada `onValueChange` y enviar el nuevo valor al padre.

Aquí está el código del componente `Slider`:

```jsx
const Slider = ({
  min = 0,
  max = 100,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <input
      type="range"
      min={min}
      max={max}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Para renderizar el componente `Slider`, use `ReactDOM.createRoot` y pase la función de devolución de llamada `onValueChange`:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Slider onValueChange={(val) => console.log(val)} />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
