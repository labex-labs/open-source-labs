# Erstellen eines einfachen Validierungstools

Nachdem wir nun die Funktion zum Prüfen auf alphanumerische Zeichen verstehen, bauen wir ein einfaches interaktives Validierungstool. Wir verwenden das integrierte `readline`-Modul von Node.js, um Benutzereingaben aus dem Terminal zu erhalten.

Erstellen Sie eine neue Datei namens `validator.js` im gleichen Verzeichnis:

1. Klicken Sie mit der rechten Maustaste in der Dateiexplorer-Panel.
2. Wählen Sie "Neue Datei" aus.
3. Benennen Sie die Datei `validator.js`.

Fügen Sie der Datei folgenden Code hinzu:

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

Speichern Sie die Datei und führen Sie sie aus mit:

```bash
node validator.js
```

Sie werden eine Willkommensnachricht und eine Eingabeaufforderung sehen, in der Sie eine Zeichenkette eingeben sollen. Versuchen Sie, verschiedene Zeichenketten einzugeben, wie z. B.:

- `hello123` (alphanumerisch)
- `Hello World` (nicht alphanumerisch wegen des Leerzeichens)
- `hello@123` (nicht alphanumerisch wegen des @-Zeichens)

Für jede Eingabe wird das Programm Ihnen mitteilen, ob die Zeichenkette alphanumerisch ist, und Sie fragen, ob Sie eine weitere Zeichenkette prüfen möchten. Geben Sie `yes` oder `y` ein, um fortzufahren, oder eine andere Antwort, um das Programm zu beenden.

Dieses interaktive Tool zeigt, wie unsere Funktion zur Alphanumerischen-Validierung in einer praktischen Anwendung eingesetzt werden kann.
