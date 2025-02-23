# Récupérer les ancêtres d'un élément

Pour récupérer les ancêtres d'un élément depuis la racine du document jusqu'à l'élément spécifié, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Node.parentNode` et une boucle `while` pour remonter l'arbre d'ancêtres de l'élément.
3. Utilisez `Array.prototype.unshift()` pour ajouter chaque nouvel ancêtre au début du tableau.

Voici un exemple de code qui met en œuvre les étapes ci-dessus :

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

Pour récupérer les ancêtres d'un élément spécifique, utilisez la méthode `querySelector()` pour sélectionner l'élément et le passer en argument à la fonction `getAncestors()`. Par exemple :

```js
getAncestors(document.querySelector("nav"));
// [document, html, body, header, nav]
```

Cela renverra un tableau de tous les ancêtres de l'élément spécifié dans l'ordre depuis la racine du document jusqu'à l'élément lui-même.
