# Cómo obtener el tamaño en bytes de una cadena en JavaScript

Para obtener el tamaño en bytes de una cadena en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Convierte la cadena en un [objeto `Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob).
3. Utiliza `Blob.size` para obtener la longitud de la cadena en bytes.

Aquí está el código JavaScript para obtener el tamaño en bytes de una cadena:

```js
const byteSize = (str) => new Blob([str]).size;
```

Puedes probar esta función con los siguientes ejemplos:

```js
byteSize("😀"); // 4
byteSize("Hello World"); // 11
```
