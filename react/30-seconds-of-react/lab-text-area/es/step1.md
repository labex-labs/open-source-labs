# Elemento `<textarea>` no controlado

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función renderiza un elemento `<textarea>` que no está controlado por el componente padre. Utiliza una función de devolución de llamada para pasar el valor de la entrada al componente padre.

Para usar esta función:

- Pase la propiedad `defaultValue` desde el componente padre como el valor inicial del campo de entrada.
- Utilice el evento `onChange` para desencadenar la devolución de llamada `onValueChange` y enviar el nuevo valor al padre.

```jsx
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Uso de ejemplo:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <TextArea
    placeholder="Insert some text here..."
    onValueChange={(val) => console.log(val)}
  />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
