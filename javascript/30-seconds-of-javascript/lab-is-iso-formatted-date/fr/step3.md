# Test avec différents formats de date

Maintenant que nous avons notre fonction de validation de base, testons-la avec différents formats de date pour comprendre son comportement avec diverses entrées.

## Création d'une suite de tests

Créons une suite de tests complète pour examiner différents formats de date :

1. Créez un nouveau fichier nommé `dateTester.js`.
2. Ajoutez le code suivant :

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Function to test different date strings
function testDate(description, dateString) {
  console.log(`Testing: ${description}`);
  console.log(`Input: "${dateString}"`);
  console.log(`Is ISO Format: ${isISOString(dateString)}`);
  console.log("-----------------------");
}

// Valid ISO date examples
testDate("Standard ISO date with timezone Z", "2023-05-12T14:30:15.123Z");
testDate("ISO date with zero milliseconds", "2020-10-12T10:10:10.000Z");

// Invalid or non-ISO format examples
testDate("Date only (no time component)", "2023-05-12");
testDate("Date and time without milliseconds", "2023-05-12T14:30:15Z");
testDate(
  "Date with time zone offset instead of Z",
  "2023-05-12T14:30:15+01:00"
);
testDate("Invalid date (month 13 does not exist)", "2023-13-12T14:30:15.123Z");
testDate("Non-date string", "Hello World");
```

3. Exécutez la suite de tests dans le terminal :

```bash
node dateTester.js
```

Vous devriez voir une sortie indiquant quelles chaînes de caractères sont des dates ISO valides et lesquelles ne le sont pas.

## Compréhension des résultats

Analysons ce qui rend chaque cas de test valide ou invalide :

1. `2023-05-12T14:30:15.123Z` - C'est valide car il suit le format ISO 8601 complet avec l'indicateur de fuseau horaire UTC (Z).

2. `2020-10-12T10:10:10.000Z` - C'est également valide, avec les millisecondes explicitement définies sur 000.

3. `2023-05-12` - C'est une date valide, mais pas au format ISO car elle manque de la composante horaire.

4. `2023-05-12T14:30:15Z` - Cela semble être au format ISO, mais il manque les millisecondes, qui sont requises dans le format ISO strict.

5. `2023-05-12T14:30:15+01:00` - Cela utilise un décalage de fuseau horaire (+01:00) au lieu de 'Z'. Bien que cela soit valide selon l'ISO 8601, notre fonction exige le format exact produit par `toISOString()`, qui utilise toujours 'Z'.

6. `2023-13-12T14:30:15.123Z` - C'est une date invalide (le mois 13 n'existe pas), donc `new Date()` créera un objet Date invalide.

7. `Hello World` - Ce n'est pas du tout une date, donc `new Date()` créera un objet Date invalide.

Notre fonction de validation vérifie spécifiquement deux conditions :

1. La chaîne de caractères doit être analysée en une date valide (pas NaN).
2. Lorsque cette date est convertie en une chaîne de caractères ISO, elle doit correspondre exactement à l'entrée originale.

Cette approche garantit que nous validons le format ISO exact produit par la méthode `toISOString()` de JavaScript.
