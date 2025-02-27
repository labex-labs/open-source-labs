# Écrire du balisage avec JSX

> Le projet React a déjà été fourni dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code dans `App.js`.

Utilisez la commande suivante pour installer les dépendances :

```bash
npm i
```

La syntaxe de balisage que vous avez vue ci-dessus s'appelle JSX. Elle est facultative, mais la plupart des projets React l'utilisent pour sa commodité.

Le JSX est plus strict que le HTML. Vous devez fermer les balises comme `<br />`. Votre composant ne peut également pas renvoyer plusieurs balises JSX. Vous devez les emballer dans un parent partagé, comme un `<h1>...</h1>` ou un emballage vide `<>...</>` :

```js
// App.js
export default function Profile() {
  return (
    <>
      <h1>Hedy Lamarr</h1>
    </>
  );
}
```

Si vous avez beaucoup de HTML à convertir en JSX, vous pouvez utiliser un [convertisseur en ligne](https://transform.tools/html-to-jsx).

Pour exécuter le projet, utilisez la commande suivante. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.

```bash
npm start
```
