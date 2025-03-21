# Как отфильтровать уникальные значения в массиве с использованием JavaScript

Для фильтрации уникальных значений в массиве с использованием JavaScript выполните следующие шаги:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте конструктор `Set` и оператор расширения (`...`), чтобы создать массив уникальных значений из исходного массива.
3. Используйте `Array.prototype.filter()`, чтобы создать массив, содержащий только неуникальные значения.
4. Определите функцию под названием `filterUnique`, которая принимает массив в качестве аргумента и применяет к нему вышеописанные шаги.
5. Вызовите функцию `filterUnique` с вашим массивом в качестве аргумента.

Ниже приведен пример кода для этого:

```js
const filterUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) !== arr.lastIndexOf(i));

filterUnique([1, 2, 2, 3, 4, 4, 5]); // [2, 4]
```

В приведенном выше фрагменте кода функция `filterUnique` принимает массив и применяет к нему конструктор `Set` и метод `Array.prototype.filter()`, чтобы вернуть массив с только неуникальными значениями.
