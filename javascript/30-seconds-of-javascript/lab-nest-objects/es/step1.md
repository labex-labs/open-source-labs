# Cómo anidar objetos utilizando recursividad en JavaScript

Para anidar objetos en una matriz plana de manera recursiva, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza la recursividad para anidar objetos que están vinculados entre sí.
3. Utiliza `Array.prototype.filter()` para filtrar los elementos donde el `id` coincida con el `link`.
4. Utiliza `Array.prototype.map()` para mapear cada elemento a un nuevo objeto que tenga una propiedad `children` que anida recursivamente los elementos basados en cuáles son los hijos del elemento actual.
5. Omite el segundo argumento, `id`, para que por defecto sea `null`, lo que indica que el objeto no está vinculado a otro (es decir, es un objeto de nivel superior).
6. Omite el tercer argumento, `link`, para utilizar `'parent_id'` como la propiedad predeterminada que vincula el objeto a otro por su `id`.

Aquí está el código:

```js
const nest = (items, id = null, link = "parent_id") =>
  items
    .filter((item) => item[link] === id)
    .map((item) => ({ ...item, children: nest(items, item.id, link) }));
```

Para utilizar la función `nest()`, crea una matriz de objetos que tengan una propiedad `id` y una propiedad `parent_id` que los vincule a otro objeto. Luego, llama a la función `nest()` y pasa la matriz como argumento. La función devolverá una nueva matriz de objetos que están anidados basados en su propiedad `parent_id`.

Por ejemplo:

```js
const comments = [
  { id: 1, parent_id: null },
  { id: 2, parent_id: 1 },
  { id: 3, parent_id: 1 },
  { id: 4, parent_id: 2 },
  { id: 5, parent_id: 4 }
];
const nestedComments = nest(comments);
// [{ id: 1, parent_id: null, children: [...] }]
```
