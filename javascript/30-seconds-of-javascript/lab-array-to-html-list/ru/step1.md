# Преобразование массива в HTML-список

Для начала кодирования запустите Терминал/SSH и введите `node`.

эта функция преобразует элементы заданного массива в теги `<li>` и добавляет их в список с заданным идентификатором.

Используйте `Array.prototype.map()` и `Document.querySelector()` для генерации списка HTML-тегов.

```js
const arrayToHTMLList = (arr, listID) =>
  (document.querySelector(`#${listID}`).innerHTML += arr
    .map((item) => `<li>${item}</li>`)
    .join(""));
```

Пример использования:

```js
arrayToHTMLList(["item 1", "item 2"], "myListID");
```
