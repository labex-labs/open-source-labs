# Асинхронное выполнение функций с использованием Web Worker

Для выполнения функции без блокировки интерфейса пользователя используйте Web Worker для запуска функции в отдельном потоке. Вот как:

1. Создайте `Worker` с использованием объекта URL `Blob`, при этом содержимым будет строковое представление функции, которую необходимо выполнить.
2. Немедленно верните возвращаемое значение вызова функции обратно.
3. Верните `Promise`, слушая события `onmessage` и `onerror` и разрешая данные, отправленные обратно из воркера, или выбрасывая ошибку.

```js
const runAsync = (fn) => {
  const worker = new Worker(
    URL.createObjectURL(new Blob([`postMessage((${fn})());`]), {
      type: "application/javascript; charset=utf-8"
    })
  );
  return new Promise((resolve, reject) => {
    worker.onmessage = ({ data }) => {
      resolve(data);
      worker.terminate();
    };
    worker.onerror = (error) => {
      reject(error);
      worker.terminate();
    };
  });
};
```

Обратите внимание, что функция, передаваемая в `runAsync`, не должна использовать замыкания, так как все строкифицируется и становится литералом. Поэтому все переменные и функции должны быть определены внутри. Вот некоторые примеры:

```js
const longRunningFunction = () => {
  let result = 0;
  for (let i = 0; i < 1000; i++)
    for (let j = 0; j < 700; j++)
      for (let k = 0; k < 300; k++) result = result + i + j + k;

  return result;
};

runAsync(longRunningFunction).then(console.log); // 209685000000
runAsync(() => 10 ** 3).then(console.log); // 1000
let outsideVariable = 50;
runAsync(() => typeof outsideVariable).then(console.log); // 'undefined'
```
