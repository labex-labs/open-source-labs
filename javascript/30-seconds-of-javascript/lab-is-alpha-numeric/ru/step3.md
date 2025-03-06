# Создание простого инструмента валидации

Теперь, когда мы понимаем функцию проверки на алфавитно-цифровые символы, давайте создадим простой интерактивный инструмент валидации. Мы будем использовать встроенный модуль `readline` в Node.js для получения ввода от пользователя из терминала.

Создайте новый файл с именем `validator.js` в той же директории:

1. Щелкните правой кнопкой мыши в панели проводника файлов.
2. Выберите "New File".
3. Назовите файл `validator.js`.

Добавьте следующий код в файл:

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

Сохраните файл и запустите его с помощью команды:

```bash
node validator.js
```

Вы увидите приветственное сообщение и приглашение ввести строку. Попробуйте ввести разные строки, например:

- `hello123` (алфавитно-цифровая)
- `Hello World` (не является алфавитно-цифровой из-за пробела)
- `hello@123` (не является алфавитно-цифровой из-за символа @)

Для каждого ввода программа сообщит, является ли строка алфавитно-цифровой, и спросит, хотите ли вы проверить другую строку. Введите `yes` или `y` для продолжения, или любое другое значение для выхода из программы.

Этот интерактивный инструмент демонстрирует, как наша функция валидации на алфавитно-цифровые символы может быть использована в практическом приложении.
