# Проверить, является ли число степенью десяти

Чтобы проверить, является ли число степенью десяти, откройте Терминал/SSH и введите `node`.

Вот код, который вы можете использовать, чтобы определить, является ли `n` степенью `10`:

```js
const isPowerOfTen = (n) => Math.log10(n) % 1 === 0;
```

Используйте функцию `isPowerOfTen()` для определения, является ли данное число степенью десяти.

```js
isPowerOfTen(1); // true
isPowerOfTen(10); // true
isPowerOfTen(20); // false
```
