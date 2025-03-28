# Создание функции для преобразования ключей в нижний регистр

Теперь, когда мы понимаем, как обращаться к ключам объекта и использовать метод `reduce()`, давайте создадим функцию, которая преобразует все ключи объекта в нижний регистр.

В интерактивной оболочке Node.js определите следующую функцию:

```javascript
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};
```

Разберем, что делает эта функция:

1. `Object.keys(obj)` получает все ключи входного объекта.
2. `.reduce()` преобразует эти ключи в новый объект.
3. Для каждого ключа мы создаем новую запись в объекте-аккумуляторе (`acc`) с:
   - Ключом, преобразованным в нижний регистр с использованием `key.toLowerCase()`.
   - Исходным значением из входного объекта (`obj[key]`).
4. Мы начинаем с пустого объекта `{}`, как начального значения для аккумулятора.
5. В конце мы возвращаем аккумулятор, который представляет собой наш новый объект с ключами в нижнем регистре.

Теперь протестируем нашу функцию с объектом `user`, который мы создали ранее:

```javascript
const lowercaseUser = lowerizeKeys(user);
lowercaseUser;
```

Вы должны увидеть следующий вывод:

```
{ name: 'John', age: 30, email: 'john@example.com' }
```

Отлично! Теперь все ключи в нижнем регистре.

Попробуем еще один пример, чтобы убедиться, что наша функция работает правильно:

```javascript
const product = {
  ProductID: 101,
  ProductName: "Laptop",
  PRICE: 999.99
};

lowerizeKeys(product);
```

Вывод должен быть таким:

```
{ productid: 101, productname: 'Laptop', price: 999.99 }
```

Наша функция работает правильно для разных объектов с различными стилями написания ключей.
