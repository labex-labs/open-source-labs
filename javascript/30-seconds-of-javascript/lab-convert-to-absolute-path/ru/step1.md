# Как преобразовать путь с тильдой в абсолютный путь в Node.js

Для начала практики программирования в Node.js откройте Терминал или SSH и введите `node`. Чтобы преобразовать путь с тильдой в абсолютный путь, используйте следующий код:

```js
const untildify = (str) =>
  str.replace(/^~($|\/|\\)/, `${require("os").homedir()}$1`);
```

В этом коде используется метод `String.prototype.replace()` с регулярным выражением и функция `os.homedir()` для замены символа `~` в начале пути на домашнюю директорию. Вот пример использования функции `untildify`:

```js
untildify("~/node"); // возвращает '/Users/aUser/node'
```
