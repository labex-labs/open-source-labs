# Explorar otras formas de comprobar cadenas alfanuméricas

Además de utilizar expresiones regulares, hay otros métodos para comprobar si una cadena es alfanumérica. Exploremos algunos de ellos creando un nuevo archivo llamado `alternative-methods.js`:

1. Haz clic derecho en el panel del explorador de archivos.
2. Selecciona "Nuevo archivo".
3. Nombrar el archivo `alternative-methods.js`.

Agrega el siguiente código al archivo:

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

Guarda el archivo y ejecútalo con:

```bash
node alternative-methods.js
```

La salida mostrará cómo se comporta cada método con diferentes cadenas de prueba y una comparación de rendimiento entre los métodos. El método de expresiones regulares suele ser el más conciso y, a menudo, el más rápido, pero es útil entender enfoques alternativos.

Veamos cada método:

1. `isAlphaNumericRegex`: Utiliza una expresión regular para coincidir solo con caracteres alfanuméricos.
2. `isAlphaNumericEvery`: Comprueba el código ASCII de cada carácter para determinar si es alfanumérico.
3. `isAlphaNumericMatch`: Elimina todos los caracteres alfanuméricos y comprueba si queda algo.

Comprender diferentes enfoques te da flexibilidad al resolver problemas de programación. Las expresiones regulares son poderosas, pero a veces pueden ser difíciles de leer. Los otros métodos pueden ser más intuitivos para algunos programadores, especialmente aquellos que no están familiarizados con los patrones de regex.
