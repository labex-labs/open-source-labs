# Codificación de una cadena a Base64

Para codificar un objeto String a una cadena ASCII codificada en base-64, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a codificar.
2. Cree un `Buffer` utilizando la cadena dada y la codificación binaria.
3. Utilice `Buffer.prototype.toString()` para devolver la cadena codificada en base-64.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const encodeToBase64 = (str) => Buffer.from(str, "binary").toString("base64");
```

Ahora puede utilizar la función `encodeToBase64()` para codificar cualquier cadena a base-64. Por ejemplo:

```js
encodeToBase64("foobar"); // 'Zm9vYmFy'
```
