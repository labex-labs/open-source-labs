# Convertir una matriz bidimensional a CSV

Para convertir una matriz bidimensional en una cadena de valores separados por comas (CSV), sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Array.prototype.map()` y `Array.prototype.join()` para combinar las matrices unidimensionales individuales (filas) en cadenas, utilizando el `delimitador` proporcionado.
3. Utiliza `Array.prototype.join()` para combinar todas las filas en una cadena CSV, separando cada fila con un salto de línea (`\n`).
4. Si quieres utilizar el delimitador predeterminado de `,`, omite el segundo argumento, `delimitador`.

Aquí hay un ejemplo del código:

```js
const arrayToCSV = (arr, delimiter = ",") =>
  arr
    .map((v) =>
      v
        .map((x) => (isNaN(x) ? `"${x.replace(/"/g, '""')}"` : x))
        .join(delimiter)
    )
    .join("\n");
```

Puedes probar la función ejecutando las siguientes líneas de código:

```js
arrayToCSV([
  ["a", "b"],
  ["c", "d"]
]); // '"a","b"\n"c","d"'
arrayToCSV(
  [
    ["a", "b"],
    ["c", "d"]
  ],
  ";"
); // '"a";"b"\n"c";"d"'
arrayToCSV([
  ["a", '"b" great'],
  ["c", 3.1415]
]);
// '"a","""b"" great"\n"c",3.1415'
```
