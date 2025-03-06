# Crear una herramienta de validación simple

Ahora que comprendemos la función de comprobación alfanumérica, construyamos una herramienta de validación interactiva simple. Utilizaremos el módulo `readline` incorporado en Node.js para obtener la entrada del usuario desde la terminal.

Crea un nuevo archivo llamado `validator.js` en el mismo directorio:

1. Haz clic derecho en el panel del explorador de archivos.
2. Selecciona "Nuevo archivo".
3. Nombrar el archivo `validator.js`.

Agrega el siguiente código al archivo:

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

Guarda el archivo y ejecútalo con:

```bash
node validator.js
```

Verás un mensaje de bienvenida y una solicitud que te pide que ingreses una cadena. Intenta ingresar diferentes cadenas, como:

- `hello123` (alfanumérica)
- `Hello World` (no alfanumérica debido al espacio)
- `hello@123` (no alfanumérica debido al símbolo @)

Para cada entrada, el programa te dirá si es alfanumérica y te preguntará si deseas comprobar otra cadena. Escribe `yes` o `y` para continuar, o cualquier otra respuesta para salir del programa.

Esta herramienta interactiva demuestra cómo se puede utilizar nuestra función de validación alfanumérica en una aplicación práctica.
