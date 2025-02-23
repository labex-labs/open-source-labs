# Индексы подстрок

Для нахождения всех индексов подстроки в данной строке следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте встроенный метод `Array.prototype.indexOf()` для поиска `searchValue` в `str`.
3. Используйте `yield`, чтобы вернуть индекс, если значение найдено, и обновить индекс `i`.
4. Используйте цикл `while`, который остановит генератор, как только значение, возвращаемое методом `Array.prototype.indexOf()`, будет равно `-1`.

Вот пример кода для реализации вышеперечисленных шагов:

```js
const indexOfSubstrings = function* (str, searchValue) {
  let i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) {
      yield r;
      i = r + 1;
    } else return;
  }
};
```

Вы можете протестировать функцию с помощью следующего кода:

```js
[...indexOfSubstrings("tiktok tok tok tik tok tik", "tik")]; // [0, 15, 23]
[...indexOfSubstrings("tutut tut tut", "tut")]; // [0, 2, 6, 10]
[...indexOfSubstrings("hello", "hi")]; // []
```
