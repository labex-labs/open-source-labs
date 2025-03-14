# Пример кода для арифметической прогрессии

Для практики программирования откройте Терминал/SSH и введите `node`.

Вот пример кода, который создает массив чисел в арифметической прогрессии. Массив начинается с заданного положительного целого числа и доходит до заданного предела:

```js
const arithmeticProgression = (n, lim) =>
  Array.from({ length: Math.ceil(lim / n) }, (_, i) => (i + 1) * n);
```

Для использования этого кода просто вызовите функцию `arithmeticProgression` с двумя аргументами: начальным положительным целым числом и пределом. Например:

```js
arithmeticProgression(5, 25); // [5, 10, 15, 20, 25]
```
