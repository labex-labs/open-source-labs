# Función para convertir una cadena de texto en un slug para URL

Para convertir una cadena de texto en un slug que se puede utilizar en una URL, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice los métodos `String.prototype.toLowerCase()` y `String.prototype.trim()` para normalizar la cadena de texto.
3. Utilice el método `String.prototype.replace()` para reemplazar los espacios, guiones y subrayados por `-`, y eliminar los caracteres especiales.
4. Implemente el siguiente código:

```js
const slugify = (str) =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_-]+/g, "-")
    .replace(/^-+|-+$/g, "");
```

5. Pruebe la función con la entrada `slugify('Hello World!');` y debería devolver la salida `'hello-world'`.
