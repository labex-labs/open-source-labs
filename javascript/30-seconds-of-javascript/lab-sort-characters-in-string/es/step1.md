# Así es como se ordenan los caracteres de una cadena:

Utiliza el siguiente código para ordenar los caracteres de una cadena en orden alfabético:

```js
const sortCharactersInString = (str) =>
  [...str].sort((a, b) => a.localeCompare(b)).join("");
```

Para comenzar, abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.

Uso de ejemplo:

```js
sortCharactersInString("cabbage"); // 'aabbceg'
```
