# Проверить, находятся ли два URL-адреса в одном источнике

Для проверки того, находятся ли два URL-адреса в одном источнике:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковать программирование.

2. Используйте `URL.protocol` и `URL.host`, чтобы проверить, имеют ли оба URL-адреса один и тот же протокол и хост.

```js
const isSameOrigin = (origin, destination) =>
  origin.protocol === destination.protocol && origin.host === destination.host;
```

3. Создайте два объекта URL с URL-адресами, которые вы хотите сравнить.

```js
const origin = new URL("https://www.30secondsofcode.org/about");
const destination = new URL("https://www.30secondsofcode.org/contact");
```

4. Вызовите функцию `isSameOrigin` с двумя объектами URL в качестве аргументов, чтобы получить логический результат.

```js
isSameOrigin(origin, destination); // true
```

5. Вы также можете протестировать функцию с другими URL-адресами, чтобы увидеть, находятся ли они в одном источнике или нет.

```js
const other = new URL("https://developer.mozilla.org");
isSameOrigin(origin, other); // false
```
