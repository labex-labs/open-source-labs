# Función para comprobar si una cadena comienza con una subcadena

Para comprobar si una cadena dada comienza con una subcadena de otra cadena, siga los pasos siguientes:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice un bucle `for...in` y el método `String.prototype.slice()` para obtener cada subcadena de la `palabra` dada, comenzando por el principio.
- Utilice el método `String.prototype.startsWith()` para comprobar la subcadena actual con el `texto`.
- Si se encuentra una subcadena coincidente, devuélvala. De lo contrario, devuelva `undefined`.

A continuación, se muestra una función de JavaScript que hace esto:

```js
const startsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(-i - 1);
    if (text.startsWith(substr)) return substr;
  }
  return undefined;
};
```

Puede llamar a esta función de la siguiente manera:

```js
startsWithSubstring("/>Lorem ipsum dolor sit amet", "<br />"); // devuelve '/>'
```
