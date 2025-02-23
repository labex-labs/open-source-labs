# Eliminar los acentos

Esta función elimina los acentos de las cadenas de texto.

- Utiliza `String.prototype.normalize()` para convertir la cadena a un formato Unicode normalizado.
- Utiliza `String.prototype.replace()` para reemplazar las marcas diacríticas en el rango de Unicode dado con cadenas vacías.

```js
const removeAccents = (str) =>
  str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
```

Para utilizar esta función, abre la Terminal/SSH y escribe `node`. Luego, llama a la función con una cadena como argumento.

```js
removeAccents("Antoine de Saint-Exupéry"); // 'Antoine de Saint-Exupery'
```
