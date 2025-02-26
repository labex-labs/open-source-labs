# React useComponentWillUnmount Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour exécuter une fonction de rappel immédiatement avant qu'un composant ne soit démonté et détruit, vous pouvez utiliser le hook `useEffect()` avec un tableau vide comme deuxième argument. Retournez la fonction de rappel fournie pour qu'elle soit exécutée une seule fois avant le nettoyage. Ce comportement est similaire à la méthode de cycle de vie `componentWillUnmount()` des composants de classe. Vous pouvez également utiliser le extrait de code suivant pour créer un hook personnalisé `useComponentWillUnmount()` qui prend une fonction `onUnmountHandler` en argument et l'exécute avant que le composant ne soit démonté :

```jsx
const useComponentWillUnmount = (onUnmountHandler) => {
  React.useEffect(
    () => () => {
      onUnmountHandler();
    },
    []
  );
};
```

Vous pouvez ensuite utiliser ce hook personnalisé dans votre composant fonctionnel comme ceci :

```jsx
const Unmounter = () => {
  useComponentWillUnmount(() => console.log("Component will unmount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Unmounter />);
```

Cela affichera "Component will unmount" dans la console lorsque le composant est sur le point d'être démonté.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
