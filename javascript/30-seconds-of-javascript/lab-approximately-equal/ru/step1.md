# Проверка на приблизительное равенство чисел в JavaScript

Для практики программирования откройте Терминал/SSH и введите `node`. Этот код проверяет, равны ли два числа друг другу приблизительно. Для этого:

- Используйте метод `Math.abs()` для сравнения абсолютной разницы двух значений с `epsilon`.
- Если вы не передаете третий аргумент, `epsilon`, функция будет использовать значение по умолчанию `0.001`.

Вот код:

```js
const approximatelyEqual = (v1, v2, epsilon = 0.001) =>
  Math.abs(v1 - v2) < epsilon;
```

Для тестирования функции вы можете вызвать ее с двумя числами в качестве аргументов, вот так:

```js
approximatelyEqual(Math.PI / 2.0, 1.5708); // true
```

Это вернет `true`, потому что `Math.PI / 2.0` приблизительно равно `1.5708` с эпсилоном `0.001`.
