# Création d'un fichier d'exemple pratique

Maintenant, créons un fichier JavaScript pour implémenter notre fonction de calcul de taille en octets de manière plus pratique. Cela montrera comment vous pourriez utiliser cette fonction dans une application du monde réel.

1. Créez un nouveau fichier dans le WebIDE. Cliquez sur l'icône "Nouveau fichier" dans la barre latérale de l'explorateur de fichiers et nommez-le `byteSizeCalculator.js`.

2. Ajoutez le code suivant au fichier :

```javascript
/**
 * Calculate the byte size of a given string.
 * @param {string} str - The string to calculate the byte size for.
 * @returns {number} The size in bytes.
 */
function calculateByteSize(str) {
  return new Blob([str]).size;
}

// Examples with different types of strings
const examples = [
  "Hello World",
  "😀",
  "The quick brown fox jumps over the lazy dog",
  "123!@#$%^&*()",
  "Hello, 世界！",
  "😀😃😄😁"
];

// Display the results
console.log("String Byte Size Calculator\n");
console.log("String".padEnd(45) + "| Characters | Bytes");
console.log("-".repeat(70));

examples.forEach((example) => {
  console.log(
    `"${example}"`.padEnd(45) +
      `| ${example.length}`.padEnd(12) +
      `| ${calculateByteSize(example)}`
  );
});
```

3. Enregistrez le fichier en appuyant sur Ctrl+S ou en sélectionnant Fichier > Enregistrer dans le menu.

4. Exécutez le fichier depuis le terminal :

```bash
node byteSizeCalculator.js
```

Vous devriez voir un résultat similaire à ceci :

```
String Byte Size Calculator

String                                      | Characters | Bytes
----------------------------------------------------------------------
"Hello World"                               | 11         | 11
"😀"                                        | 1          | 4
"The quick brown fox jumps over the lazy dog" | 43         | 43
"123!@#$%^&*()"                            | 13         | 13
"Hello, 世界!"                              | 10         | 13
"😀😃😄😁"                                  | 4          | 16
```

Ce tableau montre clairement la différence entre le nombre de caractères et la taille en octets pour différents types de chaînes de caractères.

Comprendre ces différences est crucial lorsque :

- Vous définissez des limites pour les entrées utilisateur dans les formulaires web
- Vous calculez les besoins de stockage pour les données textuelles
- Vous travaillez avec des API qui ont des limitations de taille
- Vous optimisez le transfert de données sur les réseaux
