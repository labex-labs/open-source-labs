# Обратный порядок цифр в числе

Чтобы перевернуть число с использованием JavaScript, вы можете использовать функцию `reverseNumber()` с такими шагами:

1. Преобразуйте число `n` в строку с использованием `Object.prototype.toString()`.
2. Используйте `String.prototype.split()`, `Array.prototype.reverse()` и `Array.prototype.join()`, чтобы получить перевернутое значение `n` в виде строки.
3. Преобразуйте строку обратно в число с использованием `parseFloat()`.
4. Сохраните знак числа с использованием `Math.sign()`.

Вот код для функции `reverseNumber()`:

```js
const reverseNumber = (n) =>
  parseFloat(`${n}`.split("").reverse().join("")) * Math.sign(n);
```

Вы можете протестировать функцию с этими примерами:

```js
reverseNumber(981); // 189
reverseNumber(-500); // -5
reverseNumber(73.6); // 6.37
reverseNumber(-5.23); // -32.5
```
