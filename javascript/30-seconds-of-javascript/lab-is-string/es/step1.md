# Comprobando si un valor es una cadena

Para comprobar si un valor es una cadena, utiliza la palabra clave `typeof` seguida del valor que quieres comprobar. Este método solo funciona para primitivos de tipo cadena.

Aquí hay un ejemplo de código que comprueba si un valor dado es una cadena:

```js
const isString = (val) => typeof val === "string";
```

Puedes usar la función `isString` de la siguiente manera:

```js
isString("10"); // true
```
