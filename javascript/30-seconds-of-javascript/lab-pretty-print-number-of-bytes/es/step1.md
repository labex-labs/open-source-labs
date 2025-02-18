# Convertir Bytes a una Cadena Legible para Humanos

Para convertir un número en bytes a una cadena legible para humanos, utiliza la función `prettyBytes()`. Aquí hay algunas cosas a tener en cuenta:

- La función utiliza un diccionario de unidades en forma de matriz que se accede según el exponente.
- Puedes utilizar el segundo argumento, `precision`, para truncar el número a un cierto número de dígitos. El valor predeterminado es `3`.
- Puedes utilizar el tercer argumento, `addSpace`, para agregar un espacio entre el número y la unidad. El valor predeterminado es `true`.
- La función devuelve la cadena formateada construyéndola, teniendo en cuenta las opciones proporcionadas y si el número es negativo o no.

Aquí está el código de la función `prettyBytes()`:

```js
const prettyBytes = (num, precision = 3, addSpace = true) => {
  const UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  if (Math.abs(num) < 1) return num + (addSpace ? " " : "") + UNITS[0];
  const exponent = Math.min(
    Math.floor(Math.log10(num < 0 ? -num : num) / 3),
    UNITS.length - 1
  );
  const n = Number(
    ((num < 0 ? -num : num) / 1000 ** exponent).toPrecision(precision)
  );
  return (num < 0 ? "-" : "") + n + (addSpace ? " " : "") + UNITS[exponent];
};
```

Y aquí hay algunos ejemplos de cómo usar la función `prettyBytes()`:

```js
prettyBytes(1000); // '1 KB'
prettyBytes(-27145424323.5821, 5); // '-27.145 GB'
prettyBytes(123456789, 3, false); // '123MB'
```
