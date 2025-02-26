# Lista de datos

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función renderiza una lista de elementos a partir de una matriz de valores primitivos. Puede usarse para renderizar condicionalmente una lista ordenada o no ordenada según el valor de la propiedad `isOrdered`. Para renderizar cada elemento de la matriz `data`, utiliza `Array.prototype.map()` para crear un elemento `<li>` con una `key` única para cada elemento.

```jsx
const DataList = ({ data, isOrdered = false }) => {
  const list = data.map((value, index) => (
    <li key={`${index}_${value}`}>{value}</li>
  ));

  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
};
```

A continuación, se muestra un ejemplo de cómo se puede usar este componente:

```jsx
const names = ["John", "Paul", "Mary"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <DataList data={names} />
    <DataList data={names} isOrdered={true} />
  </>
);
```

En este ejemplo, estamos pasando una matriz de nombres al componente `DataList` y lo estamos renderizando dos veces. La primera vez, estamos renderizando una lista no ordenada, mientras que la segunda vez estamos renderizando una lista ordenada.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
