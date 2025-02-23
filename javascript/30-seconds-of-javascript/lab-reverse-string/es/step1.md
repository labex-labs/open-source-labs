# Aquí está una función para invertir una cadena de texto:

Para invertir una cadena de texto, utiliza el operador de propagación (`...`) y `Array.prototype.reverse()`. Combina los caracteres para obtener una cadena de texto utilizando `Array.prototype.join()`. Aquí está el código:

```js
const reverseString = (str) => [...str].reverse().join("");
```

Uso de ejemplo:

```js
reverseString("foobar"); // 'raboof'
```
