# Comprobando valores primitivos

Para practicar la codificación, abre la Terminal o SSH y escribe `node`. Una vez que hayas hecho eso, puedes comprobar si un valor es primitivo o no siguiendo estos pasos:

1. Crea un objeto a partir del valor que quieres comprobar utilizando `Object(val)`.
2. Compara el objeto creado con el valor original utilizando el operador de desigualdad estricta `!==`.
3. Si los dos valores no son iguales, el valor original es primitivo.

Aquí está el código para la función `isPrimitive`:

```js
const isPrimitive = (val) => Object(val) !== val;
```

Puedes probar esta función con los siguientes valores:

```js
isPrimitive(null); // true
isPrimitive(undefined); // true
isPrimitive(50); // true
isPrimitive("Hello!"); // true
isPrimitive(false); // true
isPrimitive(Symbol()); // true
isPrimitive([]); // false
isPrimitive({}); // false
```

Si el valor que quieres comprobar es primitivo, la función devolverá `true`. En caso contrario, devolverá `false`.
