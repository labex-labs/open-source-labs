# Tabla de Datos

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Crea un elemento de tabla con dos columnas, `ID` y `Valor`, donde cada fila se genera dinámicamente a partir de una matriz de valores primitivos.

Para lograr esto, utiliza el método `Array.prototype.map()` para crear una nueva matriz de elementos JSX que representen cada elemento en la matriz de entrada `data` como un elemento `<tr>` con una `key` adecuada. Dentro de cada `<tr>`, agrega dos elementos `<td>` para mostrar el índice y el valor de la fila respectivamente.

A continuación, se muestra una implementación de ejemplo:

```jsx
const DataTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Valor</th>
        </tr>
      </thead>
      <tbody>
        {data.map((val, i) => (
          <tr key={`${i}_${val}`}>
            <td>{i}</td>
            <td>{val}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

Para usar este componente con una matriz de nombres de personas, por ejemplo, puedes llamarlo de la siguiente manera:

```jsx
const people = ["John", "Jesse"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <DataTable data={people} />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
