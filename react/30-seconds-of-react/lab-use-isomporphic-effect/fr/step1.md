# React useIsomporphicEffect Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour vous assurer d'utiliser correctement `useEffect()` sur le serveur et `useLayoutEffect()` sur le client, vous pouvez utiliser `typeof` pour vérifier si l'objet `Window` est défini. Si c'est le cas, renvoyez `useLayoutEffect()`, sinon renvoyez `useEffect()`. Voici un exemple de mise en œuvre de cela :

```jsx
const useIsomorphicEffect =
  typeof window !== "undefined" ? React.useLayoutEffect : React.useEffect;
```

Ensuite, dans votre code, vous pouvez utiliser `useIsomorphicEffect()` comme dans cet exemple :

```jsx
const MyApp = () => {
  useIsomorphicEffect(() => {
    window.console.log("Hello");
  }, []);

  return null;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Cela affichera 'Hello' dans la console lorsque le composant est monté et fonctionnera correctement sur le serveur et le client.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
