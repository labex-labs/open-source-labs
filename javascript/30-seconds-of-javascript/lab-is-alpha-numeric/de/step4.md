# Erkundung anderer Methoden zur Prüfung auf alphanumerische Zeichenketten

Neben der Verwendung von regulären Ausdrücken gibt es andere Methoden, um zu prüfen, ob eine Zeichenkette alphanumerisch ist. Lassen Sie uns einige davon erkunden, indem wir eine neue Datei namens `alternative-methods.js` erstellen:

1. Klicken Sie mit der rechten Maustaste in der Dateiexplorer-Panel.
2. Wählen Sie "Neue Datei" aus.
3. Benennen Sie die Datei `alternative-methods.js`.

Fügen Sie der Datei folgenden Code hinzu:

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

Speichern Sie die Datei und führen Sie sie aus mit:

```bash
node alternative-methods.js
```

Die Ausgabe zeigt, wie jede Methode mit verschiedenen Testzeichenketten performt und bietet einen Performance-Vergleich zwischen den Methoden. Die Methode mit regulären Ausdrücken ist typischerweise die kompakteste und oft auch die schnellste, aber es ist nützlich, alternative Ansätze zu verstehen.

Schauen wir uns jede Methode an:

1. `isAlphaNumericRegex`: Nutzt einen regulären Ausdruck, um nur alphanumerische Zeichen zu matchen.
2. `isAlphaNumericEvery`: Prüft den ASCII-Code jedes Zeichens, um zu bestimmen, ob es alphanumerisch ist.
3. `isAlphaNumericMatch`: Entfernt alle alphanumerischen Zeichen und prüft, ob noch etwas übrig bleibt.

Das Verständnis verschiedener Ansätze gibt Ihnen Flexibilität bei der Lösung von Programmierproblemen. Reguläre Ausdrücke sind leistungsstark, können aber manchmal schwer zu lesen sein. Die anderen Methoden könnten für einige Programmierer intuitiver sein, insbesondere für diejenigen, die nicht mit regulären Ausdrucksmustern vertraut sind.
