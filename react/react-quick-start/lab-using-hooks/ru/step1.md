# Использование хуков

> Виртуальная машина уже содержит проект React. В общем случае, вам нужно только добавить код в `App.js`.

Для установки зависимостей используйте следующую команду:

```bash
npm i
```

Функции, имена которых начинаются с `use`, называются хуками. `useState` - это встроенный хуок, предоставляемый React. Другие встроенные хуки можно найти в справочнике API. Также вы можете написать свои собственные хуки, комбинируя существующие.

Хуки более ограничены, чем другие функции. Вы можете вызывать хуки только в начале компонентов (или других хуков). Если вы хотите использовать `useState` в условиях или циклах, извлеките новый компонент и поместите его там.

В предыдущем примере у каждого `MyButton` был свой независимый `count`, и при нажатии на каждую кнопку изменялось только `count` для нажатой кнопки:

![Не используя хуки](../assets/1.png)

Однако часто вам нужно, чтобы компоненты могли делиться данными и всегда обновляться вместе.

Чтобы оба компонента `MyButton` отображали одинаковое значение `count` и обновлялись вместе, вам нужно перенести состояние из отдельных кнопок "вверх" в ближайший компонент, содержащий все они.

В этом примере это `MyApp`:

![Используя хуки](../assets/2.png)

Теперь при нажатии на любую кнопку `count` в `MyApp` изменится, что приведет к изменению обоих значений `count` в `MyButton`. Вот, как это можно выразить в коде.

Во - первых, перенесите состояние из `MyButton` в `MyApp`:

```js
// App.js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  //... мы переносим код отсюда...
}
```

Затем передайте состояние из `MyApp` в каждый `MyButton`, вместе с общим обработчиком клика. Вы можете передавать информацию в `MyButton` с использованием фигурных скобок в JSX, так же, как вы это делали ранее с встроенными тегами, такими как `<img>`:

```js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}
```

Информация, которую вы передаете так, называется пропсами. Теперь компонент `MyApp` содержит состояние `count` и обработчик события `handleClick` и передает оба эти значения в качестве пропсов в каждую кнопку.

Наконец, измените `MyButton`, чтобы он читал пропсы, переданные из родительского компонента:

```js
function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

При нажатии на кнопку срабатывает обработчик `onClick`. Каждая кнопка имеет пропс `onClick`, установленный на функцию `handleClick` внутри `MyApp`, поэтому код внутри нее выполняется. Этот код вызывает `setCount(count + 1)`, увеличивая переменную состояния `count`. Новое значение `count` передается в качестве пропса в каждую кнопку, поэтому все они показывают новое значение. Это называется "поднятием состояния вверх". Перемещая состояние вверх, вы поделили его между компонентами.

```js
import { useState } from "react";

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

Для запуска проекта используйте следующую команду. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб - страницу.

```bash
npm start
```
