# Как получить суффикс времени суток для целого числа

Для начала работы с кодом откройте Терминал/SSH и введите `node`.

Вот функция, которая преобразует целое число в строку в формате 12-часового времени с суффиксом времени суток.

Для этого используйте оператор модуля (`%`) и условные проверки.

```js
const getMeridiemSuffixOfInteger = (num) => {
  if (num === 0 || num === 24) {
    return "12am";
  } else if (num === 12) {
    return "12pm";
  } else if (num < 12) {
    return num + "am";
  } else {
    return (num % 12) + "pm";
  }
};
```

Вот несколько примеров использования этой функции:

```js
getMeridiemSuffixOfInteger(0); // '12am'
getMeridiemSuffixOfInteger(11); // '11am'
getMeridiemSuffixOfInteger(13); // '1pm'
getMeridiemSuffixOfInteger(25); // '1pm'
```

Эта функция принимает целое число в качестве аргумента и возвращает строку с суффиксом времени суток.
