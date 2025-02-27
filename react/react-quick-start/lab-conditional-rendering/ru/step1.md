# Условное рендеринг

> Виртуальная машина уже содержит проект React. В общем случае вам нужно только добавить код в `App.js`.

Установите зависимости с помощью следующей команды:

```bash
npm i
```

В React нет особого синтаксиса для записи условий. Вместо этого вы будете использовать те же приемы, что и при написании обычного JavaScript кода. Например, вы можете использовать инструкцию `if` для условного включения JSX:

```js
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

Если вы предпочитаете более компактный код, вы можете использовать условный оператор `?`. В отличие от `if`, он работает внутри JSX:

```js
return <li className="item">{isPacked ? name + " ✔" : name}</li>;
```

Когда вам не нужен else-блок, вы также можете использовать более короткую логическую синтаксис `&&`:

```js
return <li className="item">{isPacked && name + " ✔"}</li>;
```

Если prop isPacked имеет значение true, этот код возвращает другое дерево JSX. При этом некоторые элементы получают галочку в конце:

```js
// App.js
function Item({ name, isPacked }) {
  if (isPacked) {
    return <li className="item">{name} ✔</li>;
  }
  return <li className="item">{name}</li>;
}

export default function PackingList() {
  return (
    <section>
      <h1>Список вещей для упаковки Салли Райд</h1>
      <ul>
        <Item isPacked={true} name="Космический костюм" />
        <Item isPacked={true} name="Шлем с золотым листом" />
        <Item isPacked={false} name="Фото Там" />
      </ul>
    </section>
  );
}
```

Для запуска проекта используйте следующую команду. Затем вы можете обновить вкладку **Web 8080**, чтобы просмотреть веб-страницу.

```bash
npm start
```
