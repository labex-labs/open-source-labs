# Comment imbriquer des objets en utilisant la récursion en JavaScript

Pour imbriquer de manière récursive des objets dans un tableau plat, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la récursion pour imbriquer les objets qui sont liés les uns aux autres.
3. Utilisez `Array.prototype.filter()` pour filtrer les éléments dont l'`id` correspond au `link`.
4. Utilisez `Array.prototype.map()` pour mapper chaque élément à un nouvel objet qui a une propriété `children` qui imbrique de manière récursive les éléments en fonction de ceux qui sont les enfants de l'élément actuel.
5. Omettez le second argument, `id`, pour prendre la valeur par défaut `null` qui indique que l'objet n'est pas lié à un autre (c'est-à-dire qu'il s'agit d'un objet de niveau supérieur).
6. Omettez le troisième argument, `link`, pour utiliser `'parent_id'` comme propriété par défaut qui lie l'objet à un autre par son `id`.

Voici le code :

```js
const nest = (items, id = null, link = "parent_id") =>
  items
    .filter((item) => item[link] === id)
    .map((item) => ({ ...item, children: nest(items, item.id, link) }));
```

Pour utiliser la fonction `nest()`, créez un tableau d'objets qui ont une propriété `id` et une propriété `parent_id` qui les lie à un autre objet. Ensuite, appelez la fonction `nest()` et passez le tableau en argument. La fonction retournera un nouveau tableau d'objets qui sont imbriqués en fonction de leur propriété `parent_id`.

Par exemple :

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
