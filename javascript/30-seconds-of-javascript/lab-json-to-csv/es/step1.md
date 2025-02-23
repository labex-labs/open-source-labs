# Convertir JSON a CSV

Para convertir una matriz de objetos en una cadena de valores separados por comas (CSV) con columnas especificadas, use la siguiente función:

```js
const JSONtoCSV = (arr, columns, delimiter = ",") =>
  [
    columns.join(delimiter),
    ...arr.map((obj) =>
      columns.reduce(
        (acc, key) =>
          `${acc}${!acc.length ? "" : delimiter}"${!obj[key] ? "" : obj[key]}"`,
        ""
      )
    )
  ].join("\n");
```

Para usarlo, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Llame a la función `JSONtoCSV` con los siguientes argumentos:
   - `arr`: una matriz de objetos a convertir.
   - `columns`: una matriz de cadenas que especifican las columnas que se incluirán en la salida CSV.
   - `delimiter`: una cadena opcional que especifica el delimitador que se usará (el valor predeterminado es `','`).
3. La función devolverá una cadena CSV que contiene solo las columnas especificadas y los valores de los objetos.
4. Si no se especifica un delimitador, se usará el delimitador predeterminado `','`.
5. Se proporcionan ejemplos de cómo usar la función en el bloque de código siguiente.

```js
JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"]
); // 'a,b\n"1","2"\n"3","4"\n"6",""\n"","7"'

JSONtoCSV(
  [{ a: 1, b: 2 }, { a: 3, b: 4, c: 5 }, { a: 6 }, { b: 7 }],
  ["a", "b"],
  ";"
); // 'a;b\n"1";"2"\n"3";"4"\n"6";""\n"";"7"'
```
