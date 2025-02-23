# Проверка, является ли значение генераторной функцией

Для проверки того, является ли значение генераторной функцией, можно использовать функцию `isGeneratorFunction`. Чтобы начать практиковаться в написании кода, откройте Терминал/SSH и введите `node`.

Вот, как работает функция `isGeneratorFunction`:

- Она проверяет, является ли заданный аргумент генераторной функцией, используя `Object.prototype.toString()` и `Function.prototype.call()`.
- Если результат проверки равен `'[object GeneratorFunction]'`, то значение является генераторной функцией.

Вот код для функции `isGeneratorFunction`:

```js
const isGeneratorFunction = (val) =>
  Object.prototype.toString.call(val) === "[object GeneratorFunction]";
```

И вот несколько примеров использования этой функции:

```js
isGeneratorFunction(function () {}); // false
isGeneratorFunction(function* () {}); // true
```
