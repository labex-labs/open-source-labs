# Campo de entrada controlado

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este fragmento de código proporciona un elemento `<input>` controlado que utiliza una función de devolución de llamada para informar a su padre sobre cualquier actualización de su valor. Aquí está cómo funciona:

- El valor del campo de entrada controlado está determinado por la propiedad `value` que se pasa desde el padre.
- Cualquier cambio realizado en el campo de entrada por el usuario es capturado por el evento `onChange`, que desencadena la función de devolución de llamada `onValueChange` y envía el nuevo valor de vuelta al componente padre.
- Para actualizar el valor del campo de entrada, el padre debe actualizar la propiedad `value` que pasa al componente de entrada controlado.

A continuación, se muestra una implementación de ejemplo del componente `ControlledInput`, seguida de un ejemplo de uso en un componente `Form`:

```jsx
const ControlledInput = ({ value, onValueChange, ...rest }) => {
  return (
    <input
      value={value}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

const Form = () => {
  const [value, setValue] = React.useState("");

  return (
    <ControlledInput
      type="text"
      placeholder="Insert some text here..."
      value={value}
      onValueChange={setValue}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
