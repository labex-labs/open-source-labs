# Función para Obtener el Tipo de un Valor

Para obtener el tipo de un valor, utiliza la siguiente función:

```js
const getType = (v) => {
  if (v === undefined) {
    return "undefined";
  }

  if (v === null) {
    return "null";
  }

  return v.constructor.name;
};
```

- La función devuelve `'undefined'` o `'null'` si el valor es `undefined` o `null`.
- En caso contrario, devuelve el nombre del constructor utilizando `Object.prototype.constructor` y `Function.prototype.name`.

Uso de ejemplo:

```js
getType(new Set([1, 2, 3])); // 'Set'
```
