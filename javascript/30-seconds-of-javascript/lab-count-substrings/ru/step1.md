# Как подсчитывать подстроки в строке с использованием JavaScript

Если вы хотите практиковаться в написании кода, откройте Терминал/SSH и введите `node`. Эта функция JavaScript подсчитывает количество вхождений заданной подстроки в заданную строку.

Для использования этой функции следуйте шагам ниже:

1. Объявите функцию под названием `countSubstrings`, которая принимает два параметра: `str` и `searchValue`.
2. Инициализируйте две переменные: `count` и `i`.
3. Используйте метод `Array.prototype.indexOf()` для поиска `searchValue` в `str`.
4. Если значение найдено, увеличьте переменную `count` и обновите переменную `i`.
5. Используйте цикл `while`, который возвращается, как только значение, возвращаемое методом `Array.prototype.indexOf()`, равно `-1`.
6. Верните переменную `count`.

Вот код для функции `countSubstrings`:

```js
const countSubstrings = (str, searchValue) => {
  let count = 0,
    i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) [count, i] = [count + 1, r + 1];
    else return count;
  }
};
```

Вы можете протестировать функцию с использованием примеров ниже:

```js
countSubstrings("tiktok tok tok tik tok tik", "tik"); // 3
countSubstrings("tutut tut tut", "tut"); // 4
```
