# Daten anzeigen

JSX ermöglicht es Ihnen, Markup in JavaScript zu integrieren. Mit geschweiften Klammern können Sie "zurück in JavaScript wechseln", um so eine Variable aus Ihrem Code einzubetten und an den Benutzer anzuzeigen. Beispielsweise wird hier `user.name` angezeigt:

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

Sie können auch aus JSX-Attributen "in JavaScript wechseln", müssen dafür jedoch geschweifte Klammern statt Anführungszeichen verwenden. Beispielsweise übergibt `className="avatar"` als CSS-Klasse den String `"avatar"`, während `src={user.imageUrl}` den Wert der JavaScript-Variable `user.imageUrl` liest und diesen Wert als `src`-Attribut übergibt:

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
