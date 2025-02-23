# Функция с аргументами, добавленными с использованием частичной функции

Для начала практики программирования откройте Терминал/SSH и введите `node`.

Функция `partial` используется для создания новой функции, которая вызывает `fn` с `partials` в качестве первых аргументов.

- Используйте оператор расширения (`...`), чтобы добавить `partials` в начало списка аргументов `fn`.

```js
const partial =
  (fn, ...partials) =>
  (...args) =>
    fn(...partials, ...args);
```

```js
const greet = (greeting, name) => greeting + " " + name + "!";
const greetHello = partial(greet, "Hello");
greetHello("John"); // 'Hello John!'
```
