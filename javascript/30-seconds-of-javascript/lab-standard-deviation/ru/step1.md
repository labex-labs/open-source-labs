# Стандартное отклонение

Чтобы вычислить стандартное отклонение массива чисел на JavaScript, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте функцию `standardDeviation(arr, usePopulation = false)`, предоставленную ниже.
3. Передайте массив чисел в качестве первого аргумента функции.
4. Пропустите второй аргумент `usePopulation`, чтобы получить стандартное отклонение выборки. Установите его в значение `true`, чтобы получить стандартное отклонение генеральной совокупности.

```js
const standardDeviation = (arr, usePopulation = false) => {
  const mean = arr.reduce((acc, val) => acc + val, 0) / arr.length;
  return Math.sqrt(
    arr
      .reduce((acc, val) => acc.concat((val - mean) ** 2), [])
      .reduce((acc, val) => acc + val, 0) /
      (arr.length - (usePopulation ? 0 : 1))
  );
};
```

Пример использования:

```js
standardDeviation([10, 2, 38, 23, 38, 23, 21]); // 13.284434142114991 (выборка)
standardDeviation([10, 2, 38, 23, 38, 23, 21], true); // 12.29899614287479 (генеральная совокупность)
```
