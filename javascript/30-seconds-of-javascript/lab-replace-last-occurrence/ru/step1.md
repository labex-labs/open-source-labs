# Функция для замены последнего вхождения шаблона в строке

Вот функция, которая заменяет последнее вхождение шаблона в строке:

```js
const replaceLast = (str, pattern, replacement) => {
```

Для ее использования откройте Терминал/SSH и введите `node`.

- Сначала используйте `typeof`, чтобы определить, является ли `pattern` строкой или регулярным выражением.
- Если `pattern` - это строка, используйте ее как `match`.
- В противном случае используйте конструктор `RegExp` для создания нового регулярного выражения, используя `RegExp.prototype.source` из `pattern` и добавив к нему флаг `'g'`. Используйте `String.prototype.match()` и `Array.prototype.slice()`, чтобы получить последнее совпадение, если оно есть.

```js
const match =
  typeof pattern === "string"
    ? pattern
    : (str.match(new RegExp(pattern.source, "g")) || []).slice(-1)[0];
```

- Используйте `String.prototype.lastIndexOf()`, чтобы найти последнее вхождение совпадения в строке.
- Если совпадение найдено, используйте `String.prototype.slice()` и шаблонную строку (template literal), чтобы заменить совпадающую подстроку на заданную `replacement`.
- Если совпадение не найдено, верните исходную строку.

```js
  if (!match) return str;
  const last = str.lastIndexOf(match);
  return last!== -1
   ? `${str.slice(0, last)}${replacement}${str.slice(last + match.length)}`
    : str;
};
```

Вот несколько примеров использования этой функции:

```js
replaceLast("abcabdef", "ab", "gg"); // 'abcggdef'
replaceLast("abcabdef", /ab/, "gg"); // 'abcggdef'
replaceLast("abcabdef", "ad", "gg"); // 'abcabdef'
replaceLast("abcabdef", /ad/, "gg"); // 'abcabdef'
```
