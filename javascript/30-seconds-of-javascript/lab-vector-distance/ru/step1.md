# Вычисление расстояния между векторами

Для вычисления расстояния между двумя векторами следуйте шагам:

1. Откройте Терминал/SSH для начала практики в программировании.
2. Введите `node`, чтобы начать.
3. Используйте `Array.prototype.reduce()`, `Math.pow()` и `Math.sqrt()` для нахождения евклидового расстояния между векторами.
4. Примените формулу `vectorDistance`, показанную ниже:

```js
const vectorDistance = (x, y) =>
  Math.sqrt(x.reduce((acc, val, i) => acc + Math.pow(val - y[i], 2), 0));
```

5. Проверьте формулу, введя два вектора в следующем формате: `vectorDistance([10, 0, 5], [20, 0, 10]);`
6. Результатом будет расстояние между двумя векторами: `11.180339887498949`.
