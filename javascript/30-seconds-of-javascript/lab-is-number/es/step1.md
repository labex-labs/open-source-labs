# Comprobar si un valor es un número en JavaScript

Para comprobar si un valor es un número en JavaScript, puedes usar el operador `typeof` para determinar si el valor está clasificado como un primitivo de número. Para evitar problemas con `NaN`, que tiene un `typeof` igual a `number` y no es igual a sí mismo, también puedes comprobar si el valor es igual a sí mismo usando `val === val`.

Aquí hay una función de ejemplo que comprueba si un valor dado es un número:

```js
const isNumber = (val) => typeof val === "number" && val === val;
```

Puedes usar esta función de la siguiente manera:

```js
isNumber(1); // true
isNumber("1"); // false
isNumber(NaN); // false
```
