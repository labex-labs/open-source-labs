# Exploration d'autres méthodes pour vérifier les chaînes de caractères alphanumériques

En plus d'utiliser les expressions régulières, il existe d'autres méthodes pour vérifier si une chaîne de caractères est alphanumérique. Explorons-en quelques-unes en créant un nouveau fichier nommé `alternative-methods.js` :

1. Cliquez avec le bouton droit dans le panneau de l'explorateur de fichiers
2. Sélectionnez "Nouveau fichier"
3. Nommez le fichier `alternative-methods.js`

Ajoutez le code suivant au fichier :

```javascript
// Method 1: Using regular expression (our original method)
function isAlphaNumericRegex(str) {
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Method 2: Using Array.every() and checking each character
function isAlphaNumericEvery(str) {
  // If string is empty, return false
  if (str.length === 0) return false;

  return [...str].every((char) => {
    const code = char.charCodeAt(0);
    // Check if character is a digit (0-9)
    const isDigit = code >= 48 && code <= 57;
    // Check if character is a lowercase letter (a-z)
    const isLowercase = code >= 97 && code <= 122;
    // Check if character is an uppercase letter (A-Z)
    const isUppercase = code >= 65 && code <= 90;

    return isDigit || isLowercase || isUppercase;
  });
}

// Method 3: Using a combination of match() and length
function isAlphaNumericMatch(str) {
  // If string is empty, return false
  if (str.length === 0) return false;

  // Remove all alphanumeric characters and check if anything remains
  const nonAlphaNumeric = str.match(/[^a-zA-Z0-9]/g);
  return nonAlphaNumeric === null;
}

// Test strings
const testStrings = [
  "hello123",
  "HELLO123",
  "hello 123",
  "hello@123",
  "",
  "0123456789",
  "abcdefghijklmnopqrstuvwxyz"
];

// Test each method with each string
console.log("=== Testing Different Methods ===");
console.log("String\t\t\tRegex\tEvery\tMatch");
console.log("---------------------------------------------");

testStrings.forEach((str) => {
  const displayStr = str.length > 10 ? str.substring(0, 10) + "..." : str;
  const paddedStr = displayStr.padEnd(16, " ");

  const regexResult = isAlphaNumericRegex(str);
  const everyResult = isAlphaNumericEvery(str);
  const matchResult = isAlphaNumericMatch(str);

  console.log(`"${paddedStr}"\t${regexResult}\t${everyResult}\t${matchResult}`);
});

console.log("\nPerformance Comparison:");
const iterations = 1000000;
const testString = "hello123ABCxyz45";

console.time("Regex Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericRegex(testString);
}
console.timeEnd("Regex Method");

console.time("Every Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericEvery(testString);
}
console.timeEnd("Every Method");

console.time("Match Method");
for (let i = 0; i < iterations; i++) {
  isAlphaNumericMatch(testString);
}
console.timeEnd("Match Method");
```

Enregistrez le fichier et exécutez-le avec :

```bash
node alternative-methods.js
```

La sortie affichera comment chaque méthode se comporte avec différentes chaînes de test et une comparaison des performances entre les méthodes. La méthode utilisant les expressions régulières est généralement la plus concise et souvent la plus rapide, mais il est utile de comprendre les approches alternatives.

Examinons chaque méthode :

1. `isAlphaNumericRegex` : Utilise une expression régulière pour ne correspondre qu'aux caractères alphanumériques.
2. `isAlphaNumericEvery` : Vérifie le code ASCII de chaque caractère pour déterminer s'il est alphanumérique.
3. `isAlphaNumericMatch` : Supprime tous les caractères alphanumériques et vérifie s'il reste quelque chose.

Comprendre différentes approches vous offre de la flexibilité lors de la résolution de problèmes de programmation. Les expressions régulières sont puissantes mais peuvent parfois être difficiles à lire. Les autres méthodes peuvent être plus intuitives pour certains programmeurs, en particulier ceux qui ne sont pas familiers avec les motifs d'expressions régulières.
