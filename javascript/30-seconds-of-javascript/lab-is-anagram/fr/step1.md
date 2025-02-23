# Fonction JavaScript pour vérifier si une chaîne est un anagramme

Pour vérifier si une chaîne est un anagramme d'une autre chaîne, utilisez la fonction JavaScript suivante. Elle est insensible à la casse et ignore les espaces, la ponctuation et les caractères spéciaux.

```js
const isAnagram = (str1, str2) => {
  const normalize = (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]/gi, "")
      .split("")
      .sort()
      .join("");
  return normalize(str1) === normalize(str2);
};
```

Pour utiliser la fonction, ouvrez le Terminal/SSH et tapez `node`. Ensuite, appelez la fonction avec deux chaînes en arguments :

```js
isAnagram("iceman", "cinema"); // true
```

La fonction utilise `String.prototype.toLowerCase()` et `String.prototype.replace()` avec une expression régulière appropriée pour supprimer les caractères inutiles. Elle utilise également `String.prototype.split()`, `Array.prototype.sort()` et `Array.prototype.join()` sur les deux chaînes pour les normaliser et vérifier si leurs formes normalisées sont égales.
