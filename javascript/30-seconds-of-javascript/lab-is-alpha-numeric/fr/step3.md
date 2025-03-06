# Création d'un outil de validation simple

Maintenant que nous comprenons la fonction de vérification alphanumérique, construisons un outil de validation interactif simple. Nous utiliserons le module `readline` intégré à Node.js pour obtenir les entrées de l'utilisateur depuis le terminal.

Créez un nouveau fichier nommé `validator.js` dans le même répertoire :

1. Cliquez avec le bouton droit dans le panneau de l'explorateur de fichiers
2. Sélectionnez "Nouveau fichier"
3. Nommez le fichier `validator.js`

Ajoutez le code suivant au fichier :

```javascript
const readline = require("readline");

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Function to check the input
function checkInput(input) {
  if (isAlphaNumeric(input)) {
    console.log(`"${input}" is alphanumeric.`);
  } else {
    console.log(`"${input}" is NOT alphanumeric.`);
    console.log(
      "Alphanumeric strings contain only letters (A-Z, a-z) and numbers (0-9)."
    );
  }

  // Ask if the user wants to check another string
  rl.question("\nDo you want to check another string? (yes/no): ", (answer) => {
    if (answer.toLowerCase() === "yes" || answer.toLowerCase() === "y") {
      askForInput();
    } else {
      console.log("Thank you for using the alphanumeric validator!");
      rl.close();
    }
  });
}

// Function to ask for input
function askForInput() {
  rl.question("Enter a string to check if it is alphanumeric: ", (input) => {
    checkInput(input);
  });
}

// Welcome message
console.log("=== Alphanumeric String Validator ===");
console.log(
  "This tool checks if a string contains only alphanumeric characters (A-Z, a-z, 0-9).\n"
);

// Start the program
askForInput();
```

Enregistrez le fichier et exécutez-le avec :

```bash
node validator.js
```

Vous verrez un message de bienvenue et une invite vous demandant d'entrer une chaîne de caractères. Essayez d'entrer différentes chaînes, telles que :

- `hello123` (alphanumérique)
- `Hello World` (non alphanumérique en raison de l'espace)
- `hello@123` (non alphanumérique en raison du symbole @)

Pour chaque entrée, le programme vous indiquera si elle est alphanumérique et vous demandera si vous souhaitez vérifier une autre chaîne. Tapez `yes` ou `y` pour continuer, ou toute autre réponse pour quitter le programme.

Cet outil interactif montre comment notre fonction de validation alphanumérique peut être utilisée dans une application pratique.
