# Una función para comprobar si una cadena termina con una subcadena

Para comprobar si una cadena dada termina con una subcadena de otra cadena, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice un bucle `for...in` y `String.prototype.slice()` para obtener cada subcadena de la `palabra` dada, comenzando por el final.
3. Utilice `String.prototype.endsWith()` para comprobar la subcadena actual contra el `texto`.
4. Devuelva la subcadena coincidente, si se encuentra. De lo contrario, devuelva `undefined`.

A continuación, se muestra el fragmento de código para implementar los pasos anteriores:

```js
const endsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(0, i + 1);
    if (text.endsWith(substr)) return substr;
  }
  return undefined;
};
```

Puede probar la función con el siguiente ejemplo:

```js
endsWithSubstring("Lorem ipsum dolor sit amet<br /", "<br />"); // '<br /'
```
