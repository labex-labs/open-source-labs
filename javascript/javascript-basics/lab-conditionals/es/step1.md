# Condicionales

> Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

Los condicionales son estructuras de código utilizadas para probar si una expresión devuelve `true` o no. Una forma muy común de condicionales es la instrucción `if...else`. Por ejemplo:

```js
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  console.log("Yay, I love chocolate ice cream!");
} else {
  console.log("Awwww, but chocolate is my favorite…");
}
```

La expresión dentro de `if ()` es la prueba. Esto utiliza el operador de igualdad estricta (tal como se describió anteriormente) para comparar la variable `iceCream` con la cadena `chocolate` para ver si las dos son iguales. Si esta comparación devuelve `true`, se ejecuta el primer bloque de código. Si la comparación no es verdadera, se ejecuta el segundo bloque de código, después de la instrucción `else`.
