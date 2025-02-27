# Отображение данных

JSX позволяет помещать разметку в JavaScript. С использованием фигурных скобок можно “вернуться обратно” в JavaScript, чтобы вставить переменную из кода и отобразить ее для пользователя. Например, это отобразит `user.name`:

```js
// App.js
const user = {
  name: "Hedy Lamarr"
};
export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
    </>
  );
}
```

Можно также “вернуться в JavaScript” из атрибутов JSX, но для этого нужно использовать фигурные скобки вместо кавычек. Например, `className="avatar"` передает строку `"avatar"` в качестве CSS-класса, а `src={user.imageUrl}` читает значение переменной JavaScript `user.imageUrl` и передает его в качестве атрибута `src`:

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg"
};
export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img className="avatar" src={user.imageUrl} />
    </>
  );
}
```
