# Convertir CSV a una matriz

Para convertir una cadena de valores separados por comas (CSV) en una matriz bidimensional, sigue estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a codificar.
2. Utilice `Array.prototype.indexOf()` para localizar el primer carácter de nueva línea (`\n`).
3. Utilice `Array.prototype.slice()` para eliminar la primera fila (fila de títulos) si `omitFirstRow` se establece en `true`.
4. Utilice `String.prototype.split()` para crear una cadena para cada fila.
5. Utilice `String.prototype.split()` para separar los valores en cada fila utilizando el `delimitador` proporcionado.
6. Si no proporciona el segundo argumento, `delimitador`, se utilizará el delimitador predeterminado de `','`.
7. Si no proporciona el tercer argumento, `omitFirstRow`, se incluirá la primera fila (fila de títulos) de la cadena CSV.

Aquí está el código para convertir CSV a una matriz:

```js
const CSVToArray = (data, delimiter = ",", omitFirstRow = false) =>
  data
    .slice(omitFirstRow ? data.indexOf("\n") + 1 : 0)
    .split("\n")
    .map((v) => v.split(delimiter));
```

Puede utilizar los siguientes ejemplos para probar la función:

```js
CSVToArray("a,b\nc,d"); // [['a', 'b'], ['c', 'd']];
CSVToArray("a;b\nc;d", ";"); // [['a', 'b'], ['c', 'd']];
CSVToArray("col1,col2\na,b\nc,d", ",", true); // [['a', 'b'], ['c', 'd']];
```
