# Cómo utilizar el Nor Lógico en JavaScript

Para comenzar a codificar en JavaScript, accede a la Terminal/SSH y escribe `node`. El Nor Lógico comprueba si ninguno de los argumentos dados es verdadero. Para devolver el inverso del o lógico de dos valores, utiliza el operador de negación lógica (`!`). Aquí hay un ejemplo:

```js
const nor = (a, b) => !(a || b);
```

Y aquí hay algunos resultados:

```js
nor(true, true); // false
nor(true, false); // false
nor(false, false); // true
```
