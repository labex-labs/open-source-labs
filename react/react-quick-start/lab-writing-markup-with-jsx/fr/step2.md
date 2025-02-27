# Afficher des données

Le JSX vous permet d'insérer du balisage dans JavaScript. Les accolades vous permettent de "retourner dans" JavaScript pour pouvoir intégrer une variable de votre code et l'afficher à l'utilisateur. Par exemple, cela affichera `user.name` :

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

Vous pouvez également "retourner dans JavaScript" à partir d'attributs JSX, mais vous devez utiliser des accolades au lieu de guillemets. Par exemple, `className="avatar"` passe la chaîne de caractères `"avatar"` comme classe CSS, tandis que `src={user.imageUrl}` lit la valeur de la variable JavaScript `user.imageUrl`, puis passe cette valeur comme attribut `src` :

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
