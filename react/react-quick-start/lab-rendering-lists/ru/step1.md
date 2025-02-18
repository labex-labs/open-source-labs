# Рендеринг списков

> Проект React уже предоставлен в виртуальной машине (VM). Как правило, вам нужно только добавить код в файл `App.js`.

Используйте следующую команду для установки зависимостей:

```bash
npm i
```

Вы будете использовать такие функции JavaScript, как цикл `for` и метод `map()` массивов, для рендеринга списков компонентов.

Например, предположим, у вас есть массив продуктов:

```js
const products = [
  { title: "Cabbage", id: 1 },
  { title: "Garlic", id: 2 },
  { title: "Apple", id: 3 }
];
```

Внутри вашего компонента используйте метод `map()` для преобразования массива продуктов в массив элементов `<li>`:

```js
const listItems = products.map((product) => (
  <li key={product.id}>{product.title}</li>
));

return <ul>{listItems}</ul>;
```

Обратите внимание, что у `<li>` есть атрибут `key`. Для каждого элемента в списке вы должны передать строку или число, которое уникально идентифицирует этот элемент среди его соседей. Обычно ключ должен быть взят из ваших данных, например, идентификатора из базы данных. React использует ваши ключи, чтобы понять, что произошло, если вы позже вставите, удалите или измените порядок элементов.

```js
// App.js
const products = [
  { title: "Cabbage", isFruit: false, id: 1 },
  { title: "Garlic", isFruit: false, id: 2 },
  { title: "Apple", isFruit: true, id: 3 }
];

export default function ShoppingList() {
  const listItems = products.map((product) => (
    <li
      key={product.id}
      style={{
        color: product.isFruit ? "magenta" : "darkgreen"
      }}
    >
      {product.title}
    </li>
  ));

  return <ul>{listItems}</ul>;
}
```

Для запуска проекта используйте следующую команду. Затем вы можете обновить вкладку **Web 8080**, чтобы предварительно просмотреть веб - страницу.

```bash
npm start
```
