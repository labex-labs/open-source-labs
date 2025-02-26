# React useForm Hook

> `index.html` et `script.js` ont déjà été fournis dans la machine virtuelle. En général, vous n'avez qu'à ajouter du code à `script.js` et `style.css`.

Pour créer une valeur avec état à partir des champs d'un formulaire, vous pouvez utiliser le crochet `useState()` pour créer une variable d'état pour les valeurs dans le formulaire. Ensuite, créez une fonction qui met à jour la variable d'état en fonction de l'événement approprié déclenché par un champ de formulaire.

Voici une implémentation d'exemple :

```jsx
const useForm = (initialValues) => {
  const [values, setValues] = React.useState(initialValues);

  return [
    values,
    (e) => {
      setValues({
        ...values,
        [e.target.name]: e.target.value
      });
    }
  ];
};
```

Dans l'exemple ci-dessus, `useForm()` prend un objet d'état initial, crée une variable d'état `values` à l'aide de `useState()`, et renvoie un tableau avec `values` et une fonction qui met à jour `values` en fonction de l'événement passé à elle.

Vous pouvez utiliser `useForm()` dans un composant de formulaire comme ceci :

```jsx
const Form = () => {
  const initialState = { email: "", password: "" };
  const [values, setValues] = useForm(initialState);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(values);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" name="email" onChange={setValues} />
      <input type="password" name="password" onChange={setValues} />
      <button type="submit">Submit</button>
    </form>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

Dans le composant `Form`, `useForm()` est appelé avec un objet d'état initial et renvoie un tableau avec `values` et `setValues()`. La fonction `handleSubmit()` affiche l'objet `values` dans la console lorsque le formulaire est soumis. Les éléments `input` sont configurés pour mettre à jour les valeurs du formulaire à l'aide de la fonction `setValues()`.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
