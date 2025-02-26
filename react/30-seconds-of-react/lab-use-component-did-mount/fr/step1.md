# React useComponentDidMount Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour exécuter une fonction de rappel immédiatement après qu'un composant est monté, vous pouvez utiliser le hook `useEffect()` avec un tableau vide comme deuxième argument. Cela garantira que la fonction de rappel fournie est exécutée une seule fois lorsque le composant est monté. La fonction `useComponentDidMount()` présentée ci-dessous utilise ce hook pour implémenter le même comportement que la méthode de cycle de vie `componentDidMount()` des composants de classe.

```jsx
const useComponentDidMount = (onMountHandler) => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};

const Mounter = () => {
  useComponentDidMount(() => console.log("Component did mount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Mounter />);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
