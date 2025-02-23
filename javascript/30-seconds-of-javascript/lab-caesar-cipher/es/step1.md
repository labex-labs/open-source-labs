# Cifrado César

Para utilizar el cifrado César, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Llame a la función `caesarCipher` con la cadena a cifrar o descifrar, el valor de desplazamiento y un booleano que indique si se debe descifrar o no.
3. La función `caesarCipher` utiliza el operador módulo (`%`) y el operador ternario (`?`) para calcular la clave de cifrado o descifrado correcta.
4. Utiliza el operador de propagación (`...`) y `Array.prototype.map()` para iterar sobre las letras de la cadena dada.
5. Utiliza `String.prototype.charCodeAt()` y `String.fromCharCode()` para convertir cada letra adecuadamente, ignorando los caracteres especiales, espacios, etc.
6. Utiliza `Array.prototype.join()` para combinar todas las letras en una cadena.
7. Si desea descifrar una cadena cifrada, pase `true` al último parámetro, `decrypt`, cuando llame a la función `caesarCipher`.

A continuación, se muestra el código de la función `caesarCipher`:

```js
const caesarCipher = (str, shift, decrypt = false) => {
  const s = decrypt ? (26 - shift) % 26 : shift;
  const n = s > 0 ? s : 26 + (s % 26);
  return [...str]
    .map((l, i) => {
      const c = str.charCodeAt(i);
      if (c >= 65 && c <= 90)
        return String.fromCharCode(((c - 65 + n) % 26) + 65);
      if (c >= 97 && c <= 122)
        return String.fromCharCode(((c - 97 + n) % 26) + 97);
      return l;
    })
    .join("");
};
```

A continuación, se muestran algunos ejemplos de cómo utilizar la función `caesarCipher`:

```js
caesarCipher("Hello World!", -3); // 'Ebiil Tloia!'
caesarCipher("Ebiil Tloia!", 23, true); // 'Hello World!'
```
