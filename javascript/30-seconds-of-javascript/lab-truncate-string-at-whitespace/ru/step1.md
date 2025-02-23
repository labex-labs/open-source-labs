# Как обрезать строку по пробелам в JavaScript

Для практики программирования откройте Терминал/SSH и введите `node`.

Вот функция, которая обрезает строку до указанной длины, сохраняя при этом пробелы, если это возможно:

```js
const truncateStringAtWhitespace = (str, lim, ending = "...") => {
  if (str.length <= lim) return str;
  const lastSpace = str.slice(0, lim - ending.length + 1).lastIndexOf(" ");
  return str.slice(0, lastSpace > 0 ? lastSpace : lim - ending.length) + ending;
};
```

Для использования этой функции передайте в качестве первого аргумента строку, которую вы хотите обрезать, в качестве второго аргумента максимальную длину и в качестве третьего аргумента необязательную строку окончания. Если длина строки меньше или равна указанной границе, возвращается исходная строка. В противном случае функция найдет последний пробел перед ограничением и обрежет строку в этом месте, добавляя строку окончания, если она указана.

Вот несколько примеров:

```js
truncateStringAtWhitespace("short", 10); // 'short'
truncateStringAtWhitespace("not so short", 10); // 'not so...'
truncateStringAtWhitespace("trying a thing", 10); // 'trying...'
truncateStringAtWhitespace("javascripting", 10); // 'javascr...'
```
