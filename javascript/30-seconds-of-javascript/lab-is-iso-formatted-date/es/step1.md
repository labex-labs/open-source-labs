# Verificar si una cadena está en formato ISO

Para verificar si una cadena dada está en el formato ISO extendido simplificado (ISO 8601), sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el constructor `Date` para crear un objeto `Date` a partir de la cadena dada.
3. Verifica si el objeto de fecha producido es válido utilizando `Date.prototype.valueOf()` y `Number.isNaN()`.
4. Compara la representación de la fecha en formato ISO con la cadena original utilizando `Date.prototype.toISOString()`.
5. Si las cadenas coinciden y la fecha es válida, devuelve `true`. De lo contrario, devuelve `false`.

A continuación, se muestra un ejemplo de fragmento de código:

```js
const isISOString = (val) => {
  const d = new Date(val);
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

isISOString("2020-10-12T10:10:10.000Z"); // true
isISOString("2020-10-12"); // false
```

Esta función devolverá `true` si la cadena está en formato ISO y `false` en caso contrario.
