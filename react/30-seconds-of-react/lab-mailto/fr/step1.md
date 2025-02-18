# Email Link

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle (VM). En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Cette fonction crée un lien qui, lorsqu'il est cliqué, ouvre le client de messagerie de l'utilisateur et remplit un nouvel e-mail avec le sujet et le contenu du corps spécifiés. Le lien est formaté à l'aide du protocole `mailto:`.

Pour utiliser la fonction, fournissez une prop `email` avec l'adresse e-mail du destinataire, et éventuellement des props `subject` et `body` pour remplir l'e-mail avec un contenu initial. Ces props sont encodées en toute sécurité à l'aide de `encodeURIComponent` avant d'être ajoutées à l'URL du lien.

Le lien est rendu avec le contenu fourni dans `children`.

```jsx
const Mailto = ({ email, subject = "", body = "", children }) => {
  const params =
    subject || body
      ? `?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(
          body
        )}`
      : "";

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

Exemple d'utilisation :

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Mailto email="foo@bar.baz" subject="Hello & Welcome" body="Hello world!">
    Mail me!
  </Mailto>
);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
