# Comment récupérer les propriétés d'objets imbriqués à partir de chaînes de caractères représentant des chemins

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

La fonction suivante permet de récupérer un ensemble de propriétés à partir d'un objet en utilisant des sélecteurs spécifiés dans une chaîne de caractères représentant un chemin. Pour ce faire, suivez les étapes suivantes :

1. Utilisez `Array.prototype.map()` pour parcourir chaque sélecteur, et appliquez `String.prototype.replace()` pour remplacer les crochets par des points.
2. Utilisez `String.prototype.split()` pour diviser chaque sélecteur en un tableau de chaînes de caractères.
3. Utilisez `Array.prototype.filter()` pour supprimer toutes les valeurs vides.
4. Utilisez `Array.prototype.reduce()` pour récupérer la valeur indiquée par chaque sélecteur.

Voici la fonction :

```js
const get = (from, ...selectors) =>
  [...selectors].map((s) =>
    s
      .replace(/\[([^\[\]]*)\]/g, ".$1.")
      .split(".")
      .filter((t) => t !== "")
      .reduce((prev, cur) => prev && prev[cur], from)
  );
```

Vous pouvez utiliser cette fonction pour récupérer des valeurs à partir d'un objet imbriqué en utilisant une chaîne de caractères représentant un chemin. Voici un exemple :

```js
const obj = {
  selector: { to: { val: "val to select" } },
  target: [1, 2, { a: "test" }]
};
get(obj, "selector.to.val", "target[0]", "target[2].a");
// ['val to select', 1, 'test']
```
