# Создание переиспользуемого модуля

Теперь, когда у нас есть работающие функции, давайте создадим переиспользуемый JavaScript-модуль в виде файла, который мы сможем импортировать в другие проекты.

Сначала выйдите из интерактивной оболочки Node.js, нажав Ctrl+C дважды или введя `.exit` и нажав Enter.

Теперь создайте новый файл с именем `object-utils.js` в директории проекта:

1. В WebIDE перейдите в панель проводника файлов слева.
2. Щелкните правой кнопкой мыши в директории проекта и выберите "Новый файл".
3. Назовите файл `object-utils.js`.
4. Добавьте следующий код в файл:

```javascript
/**
 * Converts all keys of an object to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase
 */
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};

/**
 * Recursively converts all keys of an object and its nested objects to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase (including nested objects)
 */
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};

// Export the functions
module.exports = {
  lowerizeKeys,
  deepLowerizeKeys
};
```

Теперь создайте тестовый файл, чтобы убедиться, что наш модуль работает правильно. Создайте новый файл с именем `test.js`:

1. В WebIDE перейдите в панель проводника файлов слева.
2. Щелкните правой кнопкой мыши в директории проекта и выберите "Новый файл".
3. Назовите файл `test.js`.
4. Добавьте следующий код в файл:

```javascript
// Import the functions from our module
const { lowerizeKeys, deepLowerizeKeys } = require("./object-utils");

// Test with a simple object
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};

console.log("Original object:");
console.log(user);

console.log("\nObject with lowercase keys:");
console.log(lowerizeKeys(user));

// Test with a nested object
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

console.log("\nNested object:");
console.log(nestedObject);

console.log("\nNested object with lowercase keys (shallow):");
console.log(lowerizeKeys(nestedObject));

console.log("\nNested object with lowercase keys (deep):");
console.log(deepLowerizeKeys(nestedObject));
```

Теперь запустите тестовый файл:

```bash
node test.js
```

Вы должны увидеть вывод, похожий на следующий:

```
Original object:
{ Name: 'John', AGE: 30, Email: 'john@example.com' }

Object with lowercase keys:
{ name: 'John', age: 30, email: 'john@example.com' }

Nested object:
{
  User: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (shallow):
{
  user: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (deep):
{
  user: {
    name: 'John',
    contact: { email: 'john@example.com', phone: '123-456-7890' }
  }
}
```

Поздравляем! Вы успешно создали переиспользуемый JavaScript-модуль с функциями для преобразования ключей объекта в нижний регистр. Теперь этот модуль можно импортировать в любой из ваших JavaScript-проектов.
