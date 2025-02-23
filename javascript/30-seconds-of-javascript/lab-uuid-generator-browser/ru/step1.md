# Генерация UUID в браузере

Чтобы сгенерировать UUID, соответствующий [RFC4122](https://www.ietf.org/rfc/rfc4122.txt), версии 4, в браузере, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`.
2. Используйте метод `Crypto.getRandomValues()`, чтобы сгенерировать UUID.
3. Преобразуйте UUID в шестнадцатеричную строку с использованием метода `Number.prototype.toString()`.
4. Реализуйте следующий код:

```js
const UUIDGeneratorBrowser = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
```

5. Вызовите функцию `UUIDGeneratorBrowser()`, чтобы сгенерировать UUID. Например, `UUIDGeneratorBrowser()` вернет `'7982fcfe-5721-4632-bede-6000885be57d'`.
