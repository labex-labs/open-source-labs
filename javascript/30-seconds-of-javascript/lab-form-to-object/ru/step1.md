# Преобразование формы в объект

Для практики программирования откройте Терминал/SSH и введите `node`. Вы можете закодировать набор элементов формы в виде объекта, выполнив следующие шаги:

1. Используйте конструктор `FormData` для преобразования HTML-формы (`form`) в `FormData`.
2. Преобразуйте `FormData` в массив с использованием `Array.from()`.
3. Соберите объект из массива с использованием `Array.prototype.reduce()`.

Ниже представлен пример кода:

```js
const formToObject = (form) =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value
    }),
    {}
  );
```

Для преобразования определенной формы вы можете вызвать функцию `formToObject` и передать в качестве аргумента элемент формы:

```js
formToObject(document.querySelector("#form"));
// { email: 'test@email.com', name: 'Test Name' }
```
