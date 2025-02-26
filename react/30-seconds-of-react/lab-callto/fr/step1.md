# Lien téléphonique appelable

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour créer un lien qui appelle un numéro de téléphone, utilisez le composant `Callto`. Ce composant crée un élément `<a>` avec un attribut `href` approprié. Pour afficher le lien, spécifiez le numéro de téléphone à l'aide de la propriété `phone` et le texte du lien à l'aide de la propriété `children`.

```jsx
const Callto = ({ phone, children }) => {
  return <a href={`tel:${phone}`}>{children}</a>;
};
```

Pour utiliser le composant `Callto`, appelez la méthode `ReactDOM.render()` et passez l'élément `Callto` avec les propriétés `phone` et `children` définies.

```jsx
ReactDOM.render(
  <Callto phone="+302101234567">Appelez-moi!</Callto>,
  document.getElementById("root")
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
