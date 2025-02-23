# Cómo eliminar etiquetas HTML/XML de una cadena

Para eliminar etiquetas HTML/XML de una cadena, puedes usar una expresión regular. Sigue estos pasos:

1. Abre la Terminal/SSH
2. Escribe `node` para comenzar a practicar la codificación
3. Utiliza el siguiente código:

```js
const stripHTMLTags = (str) => str.replace(/<[^>]*>/g, "");
```

4. Prueba la función con el siguiente ejemplo:

```js
stripHTMLTags("<p><em>lorem</em> <strong>ipsum</strong></p>"); // 'lorem ipsum'
```

Esto eliminará todas las etiquetas HTML/XML de la cadena de entrada y devolverá el texto restante.
