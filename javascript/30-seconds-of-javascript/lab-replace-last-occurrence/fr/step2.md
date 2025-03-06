# Implémentation de la logique principale de la fonction

Maintenant que nous comprenons le problème, implémentons la fonctionnalité principale de notre fonction `replaceLast`. Nous allons d'abord nous concentrer sur la gestion des motifs sous forme de chaînes de caractères, puis nous aborderons les expressions régulières (regular expressions) à l'étape suivante.

Lorsque le motif est une chaîne de caractères, nous pouvons utiliser la méthode `lastIndexOf` pour trouver la position de la dernière occurrence. Une fois que nous connaissons cette position, nous pouvons utiliser la méthode `slice` pour reconstruire la chaîne de caractères en insérant le remplacement.

Mettez à jour votre fonction `replaceLast` avec l'implémentation suivante :

```javascript
function replaceLast(str, pattern, replacement) {
  // Ensure inputs are valid
  if (typeof str !== "string") {
    return str;
  }

  if (typeof pattern === "string") {
    // Find the position of the last occurrence
    const lastIndex = str.lastIndexOf(pattern);

    // If pattern not found, return original string
    if (lastIndex === -1) {
      return str;
    }

    // Rebuild the string with the replacement
    const before = str.slice(0, lastIndex);
    const after = str.slice(lastIndex + pattern.length);
    return before + replacement + after;
  }

  // We'll handle regex patterns in the next step
  return str;
}
```

Mettez à jour vos cas de test pour vérifier que la fonction gère correctement les motifs sous forme de chaînes de caractères :

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)
```

Exécutez le code à nouveau pour voir la sortie mise à jour :

```bash
node replaceLast.js
```

Vous devriez maintenant voir la dernière occurrence du motif sous forme de chaîne de caractères remplacée dans chaque cas de test. Par exemple, "Hello world JavaScript" au lieu de "Hello world world".
