# Decodificación de una cadena codificada en Base64

Para decodificar una cadena de datos que ha sido codificada utilizando codificación base-64, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Cree un `Buffer` para la cadena dada con codificación base-64.
3. Utilice `Buffer.prototype.toString()` para devolver la cadena decodificada.

A continuación, se muestra un fragmento de código de ejemplo:

```js
const atob = (str) => Buffer.from(str, "base64").toString("binary");
```

Puede probar esta función ejecutando `atob('Zm9vYmFy')`, lo que debería devolver `'foobar'`.
