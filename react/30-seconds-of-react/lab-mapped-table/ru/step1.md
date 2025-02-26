# Представление таблицы объектов

> В ВМ уже предоставлены `index.html` и `script.js`. В общем, вам нужно только добавлять код в `script.js` и `style.css`.

Данный компонент отображает таблицу с рядами, динамически создаваемыми из массива объектов и списка имен свойств. Для этого необходимо:

- Использовать `Object.keys()`, `Array.prototype.filter()`, `Array.prototype.includes()` и `Array.prototype.reduce()` для получения массива `filteredData`, содержащего все объекты с ключами, указанными в `propertyNames`.
- Отрендерить элемент `<table>` с количеством столбцов, равным количеству значений в `propertyNames`.
- Использовать `Array.prototype.map()` для отображения каждого значения в массиве `propertyNames` в виде элемента `<th>`.
- Использовать `Array.prototype.map()` для отображения каждого объекта в массиве `filteredData` в виде элемента `<tr>`, содержащего `<td>` для каждого ключа в объекте.
- Обратите внимание, что этот компонент не работает с вложенными объектами и будет работать неправильно, если внутри любого из свойств, указанных в `propertyNames`, есть вложенные объекты.

Вот код:

```jsx
const MappedTable = ({ data, propertyNames }) => {
  const filteredData = data.map((obj) =>
    Object.keys(obj)
      .filter((key) => propertyNames.includes(key))
      .reduce((acc, key) => ({ ...acc, [key]: obj[key] }), {})
  );

  return (
    <table>
      <thead>
        <tr>
          {propertyNames.map((name) => (
            <th key={`header-${name}`}>{name}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {filteredData.map((obj, i) => (
          <tr key={`row-${i}`}>
            {propertyNames.map((name) => (
              <td key={`cell-${i}-${name}`}>{obj[name]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

Вы можете использовать компонент, передав в него массив объектов и список имен свойств:

```jsx
const people = [
  { name: "John", surname: "Smith", age: 42 },
  { name: "Adam", surname: "Smith", gender: "male" }
];
const propertyNames = ["name", "surname", "age"];

ReactDOM.render(
  <MappedTable data={people} propertyNames={propertyNames} />,
  document.getElementById("root")
);
```

Пожалуйста, нажмите кнопку 'Go Live' в нижнем правом углу, чтобы запустить веб-сервис на порту 8080. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.
