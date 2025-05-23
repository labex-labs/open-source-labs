# Кодирование строки в Base64

Для кодирования объекта String в ASCII-строку, закодированную в base-64, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать программирование.
2. Создайте `Buffer` с использованием заданной строки и двоичной кодировки.
3. Используйте `Buffer.prototype.toString()`, чтобы вернуть строку, закодированную в base-64.

Вот пример фрагмента кода:

```js
const encodeToBase64 = (str) => Buffer.from(str, "binary").toString("base64");
```

Теперь вы можете использовать функцию `encodeToBase64()` для кодирования любой строки в base-64. Например:

```js
encodeToBase64("foobar"); // 'Zm9vYmFy'
```
