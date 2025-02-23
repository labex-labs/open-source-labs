# Determinando si un valor es un objeto

Para determinar si un valor pasado es un objeto, abra la Terminal/SSH y escriba `node`. Se siguen los siguientes pasos:

- El constructor `Object` crea un envoltorio de objeto para el valor dado.
- Si el valor es `null` o `undefined`, se crea y devuelve un objeto vacío.
- Si el valor no es `null` o `undefined`, se devuelve un objeto de un tipo correspondiente al valor dado.

A continuación, hay una función de ejemplo que comprueba si un valor es un objeto:

```js
const isObject = (obj) => obj === Object(obj);
```

A continuación, hay algunos ejemplos de uso de la función `isObject`:

```js
isObject([1, 2, 3, 4]); // true
isObject([]); // true
isObject(["Hello!"]); // true
isObject({ a: 1 }); // true
isObject({}); // true
isObject(true); // false
```
