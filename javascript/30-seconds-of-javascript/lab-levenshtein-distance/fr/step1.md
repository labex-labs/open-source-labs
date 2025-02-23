# Algorithme de distance de Levenshtein

Pour calculer la différence entre deux chaînes de caractères, vous pouvez utiliser l'algorithme de distance de Levenshtein. Voici comment procéder :

1. Si l'une des deux chaînes a une `longueur` de zéro, renvoyez la `longueur` de l'autre.
2. Utilisez une boucle `for` imbriquée pour itérer sur les lettres des chaînes cible et source.
3. Calculez le coût de la substitution des lettres correspondant à `i - 1` et `j - 1` dans la chaîne cible et la chaîne source respectivement (`0` si elles sont identiques, `1` sinon).
4. Utilisez `Math.min()` pour remplir chaque élément du tableau 2D avec le minimum de la cellule au-dessus incrémentée de 1, de la cellule à gauche incrémentée de 1, ou de la cellule en haut à gauche incrémentée du coût précédemment calculé.
5. Renvoyez le dernier élément de la dernière ligne du tableau produit.

Pour commencer à pratiquer ce codage, ouvrez le Terminal/SSH et tapez `node`. Voici le code que vous pouvez utiliser :

```js
const levenshteinDistance = (s, t) => {
  if (!s.length) return t.length;
  if (!t.length) return s.length;
  const arr = [];
  for (let i = 0; i <= t.length; i++) {
    arr[i] = [i];
    for (let j = 1; j <= s.length; j++) {
      arr[i][j] =
        i === 0
          ? j
          : Math.min(
              arr[i - 1][j] + 1,
              arr[i][j - 1] + 1,
              arr[i - 1][j - 1] + (s[j - 1] === t[i - 1] ? 0 : 1)
            );
    }
  }
  return arr[t.length][s.length];
};

console.log(levenshteinDistance("duck", "dark")); // 2
```
