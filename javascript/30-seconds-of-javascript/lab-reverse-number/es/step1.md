# Invirtiendo un número

Para invertir un número utilizando JavaScript, puedes utilizar la función `reverseNumber()` con los siguientes pasos:

1. Convierte el número `n` a una cadena utilizando `Object.prototype.toString()`.
2. Utiliza `String.prototype.split()`, `Array.prototype.reverse()` y `Array.prototype.join()` para obtener el valor invertido de `n` como una cadena.
3. Convierte la cadena de nuevo a un número utilizando `parseFloat()`.
4. Conserva el signo del número utilizando `Math.sign()`.

Aquí está el código de la función `reverseNumber()`:

```js
const reverseNumber = (n) =>
  parseFloat(`${n}`.split("").reverse().join("")) * Math.sign(n);
```

Puedes probar la función con estos ejemplos:

```js
reverseNumber(981); // 189
reverseNumber(-500); // -5
reverseNumber(73.6); // 6.37
reverseNumber(-5.23); // -32.5
```
