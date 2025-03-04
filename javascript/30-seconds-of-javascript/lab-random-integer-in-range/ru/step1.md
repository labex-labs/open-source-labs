# Как сгенерировать случайное целое число в заданном диапазоне с использованием JavaScript

Чтобы сгенерировать случайное целое число в заданном диапазоне с использованием JavaScript, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте метод `Math.random()` для генерации случайного числа от 0 до 1.
3. Отобразите случайное число в нужном диапазоне, умножив его на разницу между максимальным и минимальным значениями диапазона, а затем добавив минимальное значение к результату.
4. Используйте метод `Math.floor()` для округления результата до ближайшего целого числа вниз.

Вот примерный код, который реализует вышеперечисленные шаги:

```js
const randomIntegerInRange = (min, max) =>
  Math.floor(Math.random() * (max - min + 1)) + min;
```

Затем вы можете вызвать функцию `randomIntegerInRange()` с нужными минимальным и максимальным значениями, чтобы сгенерировать случайное целое число в этом диапазоне. Например:

```js
randomIntegerInRange(0, 5); // 2
```
