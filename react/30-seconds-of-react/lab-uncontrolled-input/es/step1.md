# Campo de entrada no controlado

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este código renderiza un elemento `<input>` no controlado que utiliza una función de devolución de llamada para informar a su padre sobre las actualizaciones de valor. Para utilizarlo:

- Pase el valor inicial desde el padre utilizando la propiedad `defaultValue`.
- Pase una función de devolución de llamada llamada `onValueChange` para manejar las actualizaciones de valor.
- Utilice el evento `onChange` para activar la devolución de llamada y enviar el nuevo valor al padre.

Aquí hay un ejemplo:

```jsx
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <UncontrolledInput
    type="text"
    placeholder="Insert some text here..."
    onValueChange={console.log}
  />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
