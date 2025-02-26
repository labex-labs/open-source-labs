# Elemento `<select>` no controlado

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este es un componente que renderiza un elemento `<select>` controlado. El componente acepta una matriz de valores y una función de devolución de llamada para pasar el valor seleccionado a su componente padre. Estos son los pasos para utilizar este componente:

- Utilice la propiedad `selectedValue` para establecer el valor inicial del elemento `<select>`.
- Utilice la propiedad `onValueChange` para especificar la función de devolución de llamada que se debe llamar cuando cambie el valor del elemento `<select>`.
- Utilice `Array.prototype.map()` en la matriz `values` para crear un elemento `<option>` para cada valor pasado.
- Cada elemento en `values` debe ser una matriz de dos elementos, donde el primer elemento es el `valor` del elemento y el segundo es el texto que se muestra para él.

```jsx
const Select = ({ values, onValueChange, selectedValue, ...rest }) => {
  return (
    <select
      defaultValue={selectedValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    >
      {values.map(([value, text]) => (
        <option key={value} value={value}>
          {text}
        </option>
      ))}
    </select>
  );
};
```

Este es un ejemplo de cómo utilizar este componente:

```jsx
const choices = [
  ["grapefruit", "Pomelo"],
  ["lime", "Limón"],
  ["coconut", "Coco"],
  ["mango", "Mango"]
];

ReactDOM.createRoot(document.getElementById("root")).render(
  <Select
    values={choices}
    selectedValue="lime"
    onValueChange={(val) => console.log(val)}
  />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
