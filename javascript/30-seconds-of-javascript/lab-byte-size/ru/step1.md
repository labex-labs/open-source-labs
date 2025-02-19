# Как получить размер строки в байтах на JavaScript

Чтобы получить размер строки в байтах на JavaScript, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в программировании.
2. Преобразуйте строку в [объект `Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob).
3. Используйте `Blob.size`, чтобы получить длину строки в байтах.

Вот код JavaScript для получения размера строки в байтах:

```js
const byteSize = (str) => new Blob([str]).size;
```

Вы можете протестировать эту функцию с помощью следующих примеров:

```js
byteSize("😀"); // 4
byteSize("Hello World"); // 11
```
