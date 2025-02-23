# JavaScript-функция для разбора HTTP-файлов cookie

Чтобы разобрать строку HTTP-заголовка cookie на JavaScript и вернуть объект со всеми парами имя-значение cookie, следуйте этим шагам:

- Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
- Используйте `String.prototype.split()`, чтобы разделить пары ключ-значение друг от друга.
- Используйте `Array.prototype.map()` и `String.prototype.split()`, чтобы разделить ключи от значений в каждой паре.
- Используйте `Array.prototype.reduce()` и `decodeURIComponent()`, чтобы создать объект со всеми парами ключ-значение.

Вот пример функции `parseCookie()`, которая реализует вышеперечисленные шаги:

```js
const parseCookie = (str) =>
  str
    .split(";")
    .map((v) => v.split("="))
    .reduce((acc, v) => {
      acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
      return acc;
    }, {});
```

Вы можете протестировать функцию следующим образом:

```js
parseCookie("foo=bar; equation=E%3Dmc%5E2");
// { foo: 'bar', equation: 'E=mc^2' }
```
