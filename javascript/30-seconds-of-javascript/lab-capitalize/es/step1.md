# Función de JavaScript para poner en mayúscula la primera letra de una cadena

Para poner en mayúscula la primera letra de una cadena en JavaScript, utiliza la siguiente función:

```js
const capitalize = (str, lowerRest = false) => {
  const [first, ...rest] = str;
  return (
    first.toUpperCase() +
    (lowerRest ? rest.join("").toLowerCase() : rest.join(""))
  );
};
```

Esta función utiliza la desestructuración de arrays y `String.prototype.toUpperCase()` para poner en mayúscula la primera letra de la cadena. El argumento `lowerRest` es opcional y se puede establecer en `true` para convertir el resto de la cadena a minúsculas.

A continuación, se muestra un ejemplo de cómo utilizar esta función:

```js
capitalize("fooBar"); // 'FooBar'
capitalize("fooBar", true); // 'Foobar'
```
