# Создание замороженного объекта Set в JavaScript

Чтобы создать замороженный объект `Set` в JavaScript, следуйте этим шагам:

1. Откройте Терминал/SSH и введите `node`, чтобы начать практиковаться в написании кода.
2. Используйте конструктор `Set`, чтобы создать новый объект `Set` из `iterable`.
3. Установите методы `add`, `delete` и `clear` нового объекта в `undefined`, чтобы эффективно заморозить объект.

Вот примерный фрагмент кода:

```js
const frozenSet = (iterable) => {
  const s = new Set(iterable);
  s.add = undefined;
  s.delete = undefined;
  s.clear = undefined;
  return s;
};

console.log(frozenSet([1, 2, 3, 1, 2]));
// Output: Set { 1, 2, 3, add: undefined, delete: undefined, clear: undefined }
```

Этот код создает замороженный объект `Set` из итерируемого объекта с числами и возвращает объект с методами `add`, `delete` и `clear`, установленными в `undefined`.
