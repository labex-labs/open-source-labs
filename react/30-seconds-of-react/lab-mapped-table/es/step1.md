# Vista de tabla de objetos

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este componente renderiza una tabla con filas que se crean dinámicamente a partir de una matriz de objetos y una lista de nombres de propiedades. Para lograr esto:

- Utilice `Object.keys()`, `Array.prototype.filter()`, `Array.prototype.includes()` y `Array.prototype.reduce()` para producir una matriz `filteredData` que contenga todos los objetos con las claves especificadas en `propertyNames`.
- Renderice un elemento `<table>` con un conjunto de columnas igual al número de valores en `propertyNames`.
- Utilice `Array.prototype.map()` para renderizar cada valor en la matriz `propertyNames` como un elemento `<th>`.
- Utilice `Array.prototype.map()` para renderizar cada objeto en la matriz `filteredData` como un elemento `<tr>` que contiene un `<td>` para cada clave en el objeto.
- Tenga en cuenta que este componente no funciona con objetos anidados y se romperá si hay objetos anidados dentro de cualquiera de las propiedades especificadas en `propertyNames`.

Aquí está el código:

```jsx
const MappedTable = ({ data, propertyNames }) => {
  const filteredData = data.map((obj) =>
    Object.keys(obj)
      .filter((key) => propertyNames.includes(key))
      .reduce((acc, key) => ({ ...acc, [key]: obj[key] }), {})
  );

  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map((name) => (
            <th key={`header-${name}`}>{name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((obj, i) => (
          <tr key={`row-${i}`}>
            {propertyNames.map((name) => (
              <td key={`cell-${i}-${name}`}>{obj[name]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

Puede usar el componente pasando una matriz de objetos y una lista de nombres de propiedades:

```jsx
const people = [
  { name: "John", surname: "Smith", age: 42 },
  { name: "Adam", surname: "Smith", gender: "male" }
];
const propertyNames = ["name", "surname", "age"];

ReactDOM.render(
  <MappedTable data={people} propertyNames={propertyNames} />,
  document.getElementById("root")
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
