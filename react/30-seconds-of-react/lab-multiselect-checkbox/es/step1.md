# Casilla de verificación con estado y selección múltiple

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este código renderiza una lista de casillas de verificación y envía el valor o valores seleccionados al componente padre mediante una función de devolución de llamada. Estos son los pasos para crearlo:

1. Utilice el hook `useState()` para inicializar la variable de estado `data` con la propiedad `options`.
2. Cree una función `toggle` que actualice la variable de estado `data` con la opción o opciones seleccionadas y llame a la función de devolución de llamada `onChange` con ellas.
3. Mapee la variable de estado `data` para generar casillas de verificación individuales y sus etiquetas. Asocie la función `toggle` al controlador `onClick` de cada casilla de verificación.

```jsx
const MultiselectCheckbox = ({ options, onChange }) => {
  const [data, setData] = React.useState(options);

  const toggle = (index) => {
    const newData = [...data];
    newData[index] = {
      ...newData[index],
      checked: !newData[index].checked
    };
    setData(newData);
    onChange(newData.filter((item) => item.checked));
  };

  return (
    <>
      {data.map((item, index) => (
        <label key={item.label}>
          <input
            type="checkbox"
            checked={item.checked || false}
            onChange={() => toggle(index)}
          />
          {item.label}
        </label>
      ))}
    </>
  );
};
```

Este es un ejemplo de cómo usarlo:

```jsx
const options = [{ label: "Item One" }, { label: "Item Two" }];

ReactDOM.createRoot(document.getElementById("root")).render(
  <MultiselectCheckbox
    options={options}
    onChange={(selected) => {
      console.log(selected);
    }}
  />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
