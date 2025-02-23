# Как сериализовать cookie

Для начала практики программирования откройте Терминал/SSH и введите `node`. Затем следуйте шагам, чтобы сериализовать пару имя-значение cookie в строку заголовка Set-Cookie:

1. Используйте шаблонные литералы и `encodeURIComponent()`, чтобы создать соответствующую строку.
2. Реализуйте функцию `serializeCookie`, передав параметры `name` и `val`.
3. Функция вернет строку, которая правильно сериализована.

Вот пример использования функции `serializeCookie`:

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

В этом примере функция `serializeCookie` принимает `foo` в качестве имени cookie и `bar` в качестве значения cookie и возвращает сериализованную строку cookie `foo=bar`.
