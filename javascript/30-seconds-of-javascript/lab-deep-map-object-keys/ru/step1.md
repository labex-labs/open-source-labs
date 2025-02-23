# Рекурсивное сопоставление ключей объекта

Для рекурсивного сопоставления ключей объекта следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте функцию `deepMapKeys` с предоставленным объектом и функцией, которая генерирует новые ключи.
3. Функция создает объект с теми же значениями, что и предоставленный объект, и ключами, сгенерированными путем запуска предоставленной функции для каждого ключа.
4. Перебирайте ключи объекта с использованием `Object.keys()`.
5. Создайте новый объект с теми же значениями и сопоставленными ключами с использованием `Array.prototype.reduce()` и предоставленной функции.
6. Если значение является объектом, рекурсивно вызовите `deepMapKeys` для него, чтобы также сопоставить его ключи.

```js
const deepMapKeys = (obj, fn) =>
  Array.isArray(obj)
    ? obj.map((val) => deepMapKeys(val, fn))
    : typeof obj === "object"
      ? Object.keys(obj).reduce((acc, current) => {
          const key = fn(current);
          const val = obj[current];
          acc[key] =
            val !== null && typeof val === "object"
              ? deepMapKeys(val, fn)
              : val;
          return acc;
        }, {})
      : obj;
```

Вот пример использования `deepMapKeys`:

```js
const obj = {
  foo: "1",
  nested: {
    child: {
      withArray: [
        {
          grandChild: ["hello"]
        }
      ]
    }
  }
};

const upperKeysObj = deepMapKeys(obj, (key) => key.toUpperCase());
/*
{
  "FOO":"1",
  "NESTED":{
    "CHILD":{
      "WITHARRAY":[
        {
          "GRANDCHILD":[ 'hello' ]
        }
      ]
    }
  }
}
*/
```
