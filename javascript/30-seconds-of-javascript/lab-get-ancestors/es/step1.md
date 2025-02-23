# Recuperar los ancestros de un elemento

Para recuperar los ancestros de un elemento desde la raíz del documento hasta el elemento especificado, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Node.parentNode` y un bucle `while` para subir el árbol de ancestros del elemento.
3. Utilice `Array.prototype.unshift()` para agregar cada nuevo ancestro al principio del array.

A continuación, se muestra un código de ejemplo que implementa los pasos anteriores:

```js
const getAncestors = (el) => {
  let ancestors = [];
  while (el) {
    ancestors.unshift(el);
    el = el.parentNode;
  }
  return ancestors;
};
```

Para recuperar los ancestros de un elemento específico, use el método `querySelector()` para seleccionar el elemento y páselo como argumento a la función `getAncestors()`. Por ejemplo:

```js
getAncestors(document.querySelector("nav"));
// [document, html, body, header, nav]
```

Esto devolverá un array de todos los ancestros del elemento especificado en el orden desde la raíz del documento hasta el elemento mismo.
