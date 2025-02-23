# Generar UUID en el navegador

Para generar un UUID conforme a [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) versión 4 en un navegador, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node`.
2. Utilice el método `Crypto.getRandomValues()` para generar un UUID.
3. Convierta el UUID a una cadena hexadecimal utilizando el método `Number.prototype.toString()`.
4. Implemente el siguiente código:

```js
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
```

5. Llame a la función `UUIDGeneratorBrowser()` para generar un UUID. Por ejemplo, `UUIDGeneratorBrowser()` devolvería `'7982fcfe-5721-4632-bede-6000885be57d'`.
