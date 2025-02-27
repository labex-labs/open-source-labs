# Ajouter des styles

En React, vous spécifiez une classe CSS avec `className`. Cela fonctionne de la même manière que l'attribut HTML [class](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class) :

```html
<img className="avatar" />
```

Ensuite, vous écrivez les règles CSS pour elle dans un fichier CSS séparé :

```css
/* App.css */
.avatar {
  border-radius: 50%;
}
```

React ne prescrit pas la manière dont vous ajoutez des fichiers CSS. Dans le cas le plus simple, vous ajouterez une balise `<link>` à votre HTML. Si vous utilisez un outil de construction ou un framework, consultez sa documentation pour savoir comment ajouter un fichier CSS à votre projet.

```js
// App.js
import "./App.css";
```

Vous pouvez également placer des expressions plus complexes à l'intérieur des accolades JSX, par exemple, [la concaténation de chaînes](https://javascript.info/operators#string-concatenation-with-binary) :

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg",
  imageSize: 90
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={"Photo of " + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize
        }}
      />
    </>
  );
}
```

Dans l'exemple ci-dessus, `style={{}}` n'est pas une syntaxe spéciale, mais un objet `{}` normal à l'intérieur des accolades JSX `style={ }`. Vous pouvez utiliser l'attribut `style` lorsque vos styles dépendent de variables JavaScript.
