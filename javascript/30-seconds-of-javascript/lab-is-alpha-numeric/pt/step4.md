# Explorando Outras Maneiras de Verificar Strings Alfanuméricas

Além de usar expressões regulares, existem outros métodos para verificar se uma string é alfanumérica. Vamos explorar alguns deles criando um novo arquivo chamado `alternative-methods.js`:

1.  Clique com o botão direito no painel do explorador de arquivos
2.  Selecione "Novo Arquivo"
3.  Nomeie o arquivo `alternative-methods.js`

Adicione o seguinte código ao arquivo:

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

Salve o arquivo e execute-o com:

```bash
node alternative-methods.js
```

A saída mostrará como cada método se comporta com diferentes strings de teste e uma comparação de desempenho entre os métodos. O método de expressão regular é tipicamente o mais conciso e, muitas vezes, o mais rápido, mas é útil entender abordagens alternativas.

Vamos analisar cada método:

1.  `isAlphaNumericRegex`: Usa uma expressão regular para corresponder apenas caracteres alfanuméricos.
2.  `isAlphaNumericEvery`: Verifica o código ASCII de cada caractere para determinar se ele é alfanumérico.
3.  `isAlphaNumericMatch`: Remove todos os caracteres alfanuméricos e verifica se algo permanece.

Compreender diferentes abordagens oferece flexibilidade ao resolver problemas de programação. Expressões regulares são poderosas, mas às vezes podem ser difíceis de ler. Os outros métodos podem ser mais intuitivos para alguns programadores, especialmente aqueles que não estão familiarizados com padrões de regex.
