# Fonction pour convertir une chaîne en un tableau de mots

Pour convertir une chaîne de caractères donnée en un tableau de mots, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `String.prototype.split()` avec un `pattern` fourni (par défaut, non-alphanumérique en tant qu'expression régulière) pour convertir en un tableau de chaînes de caractères.
3. Utilisez la méthode `Array.prototype.filter()` pour supprimer toutes les chaînes vides.
4. Omettez le deuxième argument, `pattern`, pour utiliser l'expression régulière par défaut.

Voici une fonction qui met en œuvre ces étapes :

```js
const words = (str, pattern = /[^a-zA-Z-]+/) =>
  str.split(pattern).filter(Boolean);
```

Vous pouvez utiliser la fonction `words()` avec différentes chaînes pour les convertir en tableaux de mots :

```js
words("I love javaScript!!"); // ['I', 'love', 'javaScript']
words("python, javaScript & coffee"); // ['python', 'javaScript', 'coffee']
```
