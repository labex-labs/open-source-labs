# Supprimer les accents

Cette fonction supprime les accents des chaînes de caractères.

- Utilisez `String.prototype.normalize()` pour convertir la chaîne en un format Unicode normalisé.
- Utilisez `String.prototype.replace()` pour remplacer les caractères diacritiques dans la plage Unicode donnée par des chaînes vides.

```js
const removeAccents = (str) =>
  str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
```

Pour utiliser cette fonction, ouvrez le Terminal/SSH et tapez `node`. Ensuite, appelez la fonction avec une chaîne en tant qu'argument.

```js
removeAccents("Antoine de Saint-Exupéry"); // 'Antoine de Saint-Exupery'
```
