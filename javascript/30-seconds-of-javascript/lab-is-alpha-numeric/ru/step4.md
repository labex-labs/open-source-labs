# Исследование других способов проверки алфавитно-цифровых строк

Кроме использования регулярных выражений, существуют и другие методы проверки, является ли строка алфавитно-цифровой. Давайте рассмотрим некоторые из них, создав новый файл с именем `alternative-methods.js`:

1. Щелкните правой кнопкой мыши в панели проводника файлов.
2. Выберите "New File".
3. Назовите файл `alternative-methods.js`.

Добавьте следующий код в файл:

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

Сохраните файл и запустите его с помощью команды:

```bash
node alternative-methods.js
```

Вывод показывает, как каждый метод работает с разными тестовыми строками, а также сравнение производительности между методами. Метод с использованием регулярного выражения обычно является наиболее лаконичным и часто самым быстрым, но полезно знать и альтернативные подходы.

Рассмотрим каждый метод:

1. `isAlphaNumericRegex`: Использует регулярное выражение для сопоставления только алфавитно-цифровых символов.
2. `isAlphaNumericEvery`: Проверяет ASCII-код каждого символа, чтобы определить, является ли он алфавитно-цифровым.
3. `isAlphaNumericMatch`: Удаляет все алфавитно-цифровые символы и проверяет, осталось ли что-то.

Понимание разных подходов дает вам гибкость при решении программистских задач. Регулярные выражения мощны, но иногда могут быть трудно читаемы. Другие методы могут быть более интуитивно понятными для некоторых программистов, особенно для тех, кто не знаком с шаблонами регулярных выражений.
