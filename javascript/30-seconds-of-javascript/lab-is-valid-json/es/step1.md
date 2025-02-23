# Comprobar si una cadena es un JSON válido

Para comprobar si una cadena dada es un JSON válido, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `JSON.parse()` y un bloque `try...catch` para comprobar si la cadena proporcionada es un JSON válido.
3. Si la cadena es válida, devuelva `true`. En caso contrario, devuelva `false`.

A continuación, se muestra un fragmento de código de ejemplo que implementa esta lógica:

```js
const isValidJSON = (str) => {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
};
```

Puede probar esta función con diferentes cadenas de entrada, como esta:

```js
isValidJSON('{"name":"Adam","age":20}'); // true
isValidJSON('{"name":"Adam",age:"20"}'); // false
isValidJSON(null); // false
```

En el último ejemplo, `null` no es una cadena JSON válida, por lo que la función devuelve `false`.
