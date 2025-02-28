# Как поменять регистр символов в строке на JavaScript

Для того чтобы поменять регистр символов в строке на JavaScript, следуйте шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте оператор расширения (`...`), чтобы преобразовать входную строку `str` в массив символов.
3. Используйте `String.prototype.toLowerCase()` и `String.prototype.toUpperCase()`, чтобы преобразовать строчные символы в прописные и наоборот.
4. Используйте `Array.prototype.map()`, чтобы применить преобразование к каждому символу, и `Array.prototype.join()`, чтобы объединить символы обратно в строку.
5. Обратите внимание, что если поменять регистр символов в строке дважды, это не обязательно приведет к исходной строке.

Ниже представлен пример кода, демонстрирующий, как поменять регистр символов в строке на JavaScript:

```js
const swapCase = (str) =>
  [...str]
    .map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))
    .join("");

swapCase("Hello world!"); // Output: 'hELLO WORLD!'
```
