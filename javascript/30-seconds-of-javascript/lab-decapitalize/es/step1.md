# Función de JavaScript para descapitalizar una cadena

Para descapitalizar la primera letra de una cadena, utiliza la siguiente función de JavaScript:

```js
const decapitalize = ([first, ...rest], upperRest = false) => {
  return (
    first.toLowerCase() +
    (upperRest ? rest.join("").toUpperCase() : rest.join(""))
  );
};
```

Para utilizar esta función, abre la Terminal/SSH y escribe `node`. Luego, llama a la función `decapitalize`, pasando como primer argumento la cadena que quieres descapitalizar.

Opcionalmente, puedes establecer el segundo argumento `upperRest` en `true` para convertir el resto de la cadena a mayúsculas. Si no se proporciona `upperRest`, el valor predeterminado es `false`.

Aquí hay algunos ejemplos:

```js
decapitalize("FooBar"); // 'fooBar'
decapitalize("FooBar", true); // 'fOOBAR'
```
