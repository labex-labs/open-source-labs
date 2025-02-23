# Comprobando espacios en blanco en una cadena

Para comprobar si una cadena contiene caracteres en blanco, siga los pasos siguientes:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice `RegExp.prototype.test()` con una expresión regular adecuada para comprobar si la cadena dada contiene caracteres en blanco.
- Aquí hay un fragmento de código de ejemplo:

  ```js
  const containsWhitespace = (str) => /\s/.test(str);
  ```

- Para probar la función, llame a `containsWhitespace` con una cadena como argumento. Devolverá `true` si la cadena contiene caracteres en blanco, de lo contrario `false`.

  ```js
  containsWhitespace("lorem"); // false
  containsWhitespace("lorem ipsum"); // true
  ```
