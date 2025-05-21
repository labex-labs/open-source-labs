# Создание практического примера файла

Теперь давайте создадим JavaScript-файл, чтобы реализовать нашу функцию для вычисления размера строки в байтах более практичным способом. Это продемонстрирует, как вы можете использовать эту функцию в реальном приложении.

1. Создайте новый файл в WebIDE. Нажмите на иконку "Новый файл" в боковой панели проводника файлов и назовите его `byteSizeCalculator.js`.

2. Добавьте следующий код в файл:

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

3. Сохраните файл, нажав Ctrl+S или выбрав "Файл > Сохранить" из меню.

4. Запустите файл из терминала:

```bash
node byteSizeCalculator.js
```

Вы должны увидеть вывод, похожий на следующий:

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

Эта таблица четко показывает разницу между количеством символов и размером в байтах для разных типов строк.

Понимание этих различий является важным, когда:

- Вы устанавливаете ограничения на пользовательский ввод в веб-формах
- Вычисляете требования к хранению текстовых данных
- Работаете с API, которые имеют ограничения по размеру
- Оптимизируете передачу данных по сети
