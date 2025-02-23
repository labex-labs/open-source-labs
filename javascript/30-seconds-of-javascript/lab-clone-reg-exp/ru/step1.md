# Клонирование регулярного выражения

Для клонирования регулярного выражения используйте конструктор `RegExp`, `RegExp.prototype.source` и `RegExp.prototype.flags`.

```js
const cloneRegExp = (regExp) => new RegExp(regExp.source, regExp.flags);
```

Этот код создаст клон заданного регулярного выражения. Например:

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp!== regExp2
```
