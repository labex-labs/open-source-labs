# CSV a JSON

Para convertir una cadena de valores separados por comas (CSV) en una matriz bidimensional de objetos y usarlo para practicar la codificación, abre la Terminal/SSH y escribe `node`. La primera fila de la cadena se utiliza como fila de títulos. Estos son los pasos para convertir CSV a JSON:

1. Utiliza `Array.prototype.indexOf()` para encontrar el primer carácter de nueva línea (`\n`).
2. Utiliza `Array.prototype.slice()` para eliminar la primera fila (fila de títulos) y `String.prototype.split()` para separarla en valores, utilizando el `delimitador` proporcionado.
3. Utiliza `String.prototype.split()` para crear una cadena para cada fila.
4. Utiliza `String.prototype.split()` para separar los valores en cada fila, utilizando el `delimitador` proporcionado.
5. Utiliza `Array.prototype.reduce()` para crear un objeto para los valores de cada fila, con las claves analizadas a partir de la fila de títulos.
6. Omite el segundo argumento, `delimitador`, para utilizar un delimitador predeterminado de `,`.

Aquí está el código:

```js
const CSVToJSON = (data, delimiter = ",") => {
  const titles = data.slice(0, data.indexOf("\n")).split(delimiter);
  return data
    .slice(data.indexOf("\n") + 1)
    .split("\n")
    .map((v) => {
      const values = v.split(delimiter);
      return titles.reduce(
        (obj, title, index) => ((obj[title] = values[index]), obj),
        {}
      );
    });
};
```

Para probar la función, utiliza los siguientes ejemplos:

```js
CSVToJSON("col1,col2\na,b\nc,d");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
CSVToJSON("col1;col2\na;b\nc;d", ";");
// [{'col1': 'a', 'col2': 'b'}, {'col1': 'c', 'col2': 'd'}];
```
