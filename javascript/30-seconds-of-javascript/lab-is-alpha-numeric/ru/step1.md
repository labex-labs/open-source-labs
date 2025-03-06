# Понимание алфавитно-цифровых символов

Алфавитно-цифровые символы состоят из 26 букв английского алфавита (как заглавных A-Z, так и строчных a-z) и 10 цифр (0-9). Когда мы проверяем, является ли строка алфавитно-цифровой, мы проверяем, что она содержит только эти символы и ничего больше.

В JavaScript мы можем проверять на наличие алфавитно-цифровых символов с использованием регулярных выражений (regular expressions). Регулярные выражения (regex) - это шаблоны, используемые для сопоставления комбинаций символов в строках.

Давайте начнем с открытия нашего редактора кода. В WebIDE перейдите к проводнику файлов слева и создайте новый JavaScript-файл:

1. Щелкните правой кнопкой мыши в панели проводника файлов.
2. Выберите "New File".
3. Назовите файл `alphanumeric.js`.

После создания файла он должен автоматически открыться в редакторе. Если это не произошло, кликните на `alphanumeric.js` в проводнике файлов, чтобы открыть его.

![new-file](../assets/screenshot-20250306-K5AOWF7Z@2x.png)

Теперь введите следующий код:

```javascript
// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  // Using regular expression to check for alphanumeric characters
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Example usage
console.log("Is 'hello123' alphanumeric?", isAlphaNumeric("hello123"));
console.log("Is '123' alphanumeric?", isAlphaNumeric("123"));
console.log("Is 'hello 123' alphanumeric?", isAlphaNumeric("hello 123"));
console.log("Is 'hello@123' alphanumeric?", isAlphaNumeric("hello@123"));
```

Сохраните файл, нажав `Ctrl+S` или выбрав "File" > "Save" в меню.

Теперь запустим этот JavaScript-файл, чтобы увидеть результат. Откройте терминал в WebIDE, выбрав "Terminal" > "New Terminal" в меню или нажав `` Ctrl+` ``.

В терминале выполните следующую команду:

```bash
node alphanumeric.js
```

Вы должны увидеть следующий вывод:

```
Is 'hello123' alphanumeric? true
Is '123' alphanumeric? true
Is 'hello 123' alphanumeric? false
Is 'hello@123' alphanumeric? false
```

Этот вывод показывает, что наша функция правильно определяет `hello123` и `123` как алфавитно-цифровые строки, в то время как `hello 123` (содержит пробел) и `hello@123` (содержит специальный символ @) не являются алфавитно-цифровыми.
