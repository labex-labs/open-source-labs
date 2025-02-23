# Cómo generar una cadena alfanumérica aleatoria en JavaScript

Para generar una cadena aleatoria de caracteres alfanuméricos en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Cree una nueva matriz con la longitud especificada utilizando `Array.from()`.
3. Genere un número de punto flotante aleatorio utilizando `Math.random()`.
4. Convierta el número a una cadena alfanumérica utilizando `Number.prototype.toString()` con un valor de `radix` de `36`.
5. Quite la parte entera y el punto decimal de cada número generado utilizando `String.prototype.slice()`.
6. Repita este proceso tantas veces como sea necesario, hasta `length`, utilizando `Array.prototype.some()`, ya que produce una cadena de longitud variable cada vez.
7. Corte la cadena generada si es más larga que la longitud dada utilizando `String.prototype.slice()`.
8. Devuelva la cadena generada.

Aquí está el código:

```js
const randomAlphaNumeric = (length) => {
  let s = "";
  Array.from({ length }).some(() => {
    s += Math.random().toString(36).slice(2);
    return s.length >= length;
  });
  return s.slice(0, length);
};
```

Puede llamar a la función `randomAlphaNumeric()` con la longitud deseada como argumento. Por ejemplo:

```js
randomAlphaNumeric(5); // '0afad'
```
