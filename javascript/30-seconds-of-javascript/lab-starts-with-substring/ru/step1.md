# Функция для проверки, начинается ли строка с подстроки

Для проверки, начинается ли заданная строка с подстроки другой строки, следуйте шагам ниже:

- Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
- Используйте цикл `for...in` и метод `String.prototype.slice()` для получения каждой подстроки заданного `word`, начиная с начала.
- Используйте метод `String.prototype.startsWith()` для проверки текущей подстроки с `text`.
- Если найдена совпадающая подстрока, верните ее. В противном случае верните `undefined`.

Вот JavaScript-функция, которая делает это:

```js
const startsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(-i - 1);
    if (text.startsWith(substr)) return substr;
  }
  return undefined;
};
```

Вы можете вызвать эту функцию следующим образом:

```js
startsWithSubstring("/>Lorem ipsum dolor sit amet", "<br />"); // возвращает '/>'
```
