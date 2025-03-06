# Создание функции для проверки строк дат в формате ISO

На этом этапе мы создадим функцию на JavaScript, которая будет проверять, является ли заданная строка допустимой строкой даты в формате ISO 8601.

## Создание функции проверки

Давайте создадим новый файл JavaScript для нашего валидатора дат в формате ISO:

1. В WebIDE нажмите на значок "Explorer" в левой боковой панели.
2. Щелкните правой кнопкой мыши в проводнике файлов и выберите "New File".
3. Назовите файл `isISODate.js` и нажмите Enter.
4. Добавьте следующий код в файл:

```javascript
/**
 * Checks if a string is a valid ISO 8601 formatted date string
 * @param {string} val - The string to check
 * @return {boolean} - Returns true if the string is in ISO format, false otherwise
 */
const isISOString = (val) => {
  // Create a Date object from the input string
  const d = new Date(val);

  // Check if the date is valid (not NaN) and if the ISO string matches the original
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

// Export the function so we can use it elsewhere
module.exports = isISOString;
```

Давайте разберем, как работает эта функция:

1. `new Date(val)` создает объект Date из входной строки.
2. `d.valueOf()` возвращает числовое значение временной метки (миллисекунды с 1 января 1970 года).
3. `Number.isNaN(d.valueOf())` проверяет, является ли дата недействительной (NaN означает "Not a Number").
4. `d.toISOString() === val` проверяет, что преобразование объекта Date обратно в строку в формате ISO совпадает с исходным входом.

## Тестирование нашей функции

Теперь давайте создадим простой тестовый файл, чтобы проверить нашу функцию:

1. Создайте еще один файл с именем `testISO.js`.
2. Добавьте следующий код:

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Test with a valid ISO formatted date
console.log("Testing a valid ISO date:");
console.log("2020-10-12T10:10:10.000Z");
console.log("Result:", isISOString("2020-10-12T10:10:10.000Z"));
console.log();

// Test with an invalid format
console.log("Testing a non-ISO date:");
console.log("2020-10-12");
console.log("Result:", isISOString("2020-10-12"));
```

3. Запустите тестовый файл с помощью Node.js:

```bash
node testISO.js
```

Вы должны увидеть вывод, похожий на следующий:

```
Testing a valid ISO date:
2020-10-12T10:10:10.000Z
Result: true

Testing a non-ISO date:
2020-10-12
Result: false
```

Это показывает, что наша функция правильно определяет, что "2020-10-12T10:10:10.000Z" является допустимой строкой даты в формате ISO, а "2020-10-12" - нет.
