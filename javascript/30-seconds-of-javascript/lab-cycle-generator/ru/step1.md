# Инструкции по генератору цикла

Для начала практики программирования откройте Терминал/SSH и введите `node`. Затем создайте генератор, который будет бесконечно перебирать заданный массив. Вот шаги:

1. Используйте неограниченный цикл `while`, который будет `возвращать` значение каждый раз, когда вызывается `Generator.prototype.next()`.
2. Используйте оператор модуля (`%`) с `Array.prototype.length`, чтобы получить индекс следующего значения, и увеличьте счетчик после каждой инструкции `yield`.

Вот пример функции `cycleGenerator`:

```js
const cycleGenerator = function* (arr) {
  let i = 0;
  while (true) {
    yield arr[i % arr.length];
    i++;
  }
};
```

Затем вы можете использовать функцию следующим образом:

```js
const binaryCycle = cycleGenerator([0, 1]);
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
```

Согласно этим инструкциям, вы можете создать генератор цикла, который будет бесконечно перебирать любой массив.
