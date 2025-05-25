# Exibindo Dados

JSX permite que você coloque marcação em JavaScript. Chaves permitem que você "escape" de volta para JavaScript para que você possa embutir alguma variável do seu código e exibi-la ao usuário. Por exemplo, isso exibirá `user.name`:

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

Você também pode "escapar para JavaScript" de atributos JSX, mas você precisa usar chaves em vez de aspas. Por exemplo, `className="avatar"` passa a string `"avatar"` como a classe CSS, mas `src={user.imageUrl}` lê o valor da variável JavaScript `user.imageUrl` e, em seguida, passa esse valor como o atributo `src`:

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
