# Debounce Promise

Чтобы создать функцию, которая возвращает промис и имеет защиту от "дребезга", задерживая вызов предоставленной функции до тех пор, пока не пройдет как минимум `ms` миллисекунд с момента последнего вызова, используйте следующие шаги:

1. Каждый раз, когда функция с защитой от "дребезга" вызывается, отмените текущий отложенный таймаут с помощью `clearTimeout()`, а затем используйте `setTimeout()`, чтобы создать новый таймаут, который задерживает вызов функции до тех пор, пока не пройдет как минимум `ms` миллисекунд.
2. Используйте `Function.prototype.apply()`, чтобы применить контекст `this` к функции и передать необходимые аргументы.
3. Создайте новый `Promise` и добавьте его `resolve` и `reject` коллбэки в стек ожидающих промисов.
4. Когда вызывается `setTimeout()`, скопируйте текущий стек (так как он может измениться между вызовом предоставленной функции и ее разрешением), очистите его и вызовите предоставленную функцию.
5. Когда предоставленная функция разрешается/отклоняется, разрешите/отклоните все промисы в стеке (скопированный при вызове функции) с возвращенными данными.
6. Игнорируйте второй аргумент, `ms`, чтобы установить таймаут по умолчанию в `0` мс.

Вот код для функции `debouncePromise()`:

```js
const debouncePromise = (fn, ms = 0) => {
  let timeoutId;
  const pending = [];
  return (...args) =>
    new Promise((res, rej) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        const currentPending = [...pending];
        pending.length = 0;
        Promise.resolve(fn.apply(this, args)).then(
          (data) => {
            currentPending.forEach(({ resolve }) => resolve(data));
          },
          (error) => {
            currentPending.forEach(({ reject }) => reject(error));
          }
        );
      }, ms);
      pending.push({ resolve: res, reject: rej });
    });
};
```

Вот пример использования `debouncePromise()`:

```js
const fn = (arg) =>
  new Promise((resolve) => {
    setTimeout(resolve, 1000, ["resolved", arg]);
  });
const debounced = debouncePromise(fn, 200);
debounced("foo").then(console.log);
debounced("bar").then(console.log);
// В обоих случаях будет выведено ['resolved', 'bar']
```
