# Comprobar si un valor es un símbolo en JavaScript

Para comprobar si un valor es un tipo primitivo símbolo en JavaScript, puedes utilizar el operador `typeof`. Aquí hay un fragmento de código de ejemplo que puedes utilizar:

```js
const isSymbol = (val) => typeof val === "symbol";
```

Puedes llamar a la función `isSymbol` y pasar un símbolo como argumento para comprobar si devuelve `true`. Aquí hay un ejemplo:

```js
isSymbol(Symbol("x")); // true
```
