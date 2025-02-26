# React useForm-Hook

> `index.html` und `script.js` wurden bereits in der VM bereitgestellt. Im Allgemeinen müssen Sie nur Code in `script.js` und `style.css` hinzufügen.

Um einen zustandsbehafteten Wert aus den Feldern eines Formulars zu erstellen, können Sie den `useState()`-Hook verwenden, um eine Zustandsvariable für die Werte im Formular zu erstellen. Anschließend erstellen Sie eine Funktion, die die Zustandsvariable basierend auf dem entsprechenden Ereignis aktualisiert, das von einem Formularfeld ausgelöst wird.

Hier ist eine Beispielimplementierung:

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

Im obigen Beispiel nimmt `useForm()` ein initiales Zustandsobjekt, erstellt eine Zustandsvariable `values` mithilfe von `useState()` und gibt ein Array zurück, das `values` und eine Funktion enthält, die `values` basierend auf dem an sie übergebenen Ereignis aktualisiert.

Sie können `useForm()` in einem Formular-Component wie folgt verwenden:

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

Im `Form`-Component wird `useForm()` mit einem initialen Zustandsobjekt aufgerufen und gibt ein Array zurück, das `values` und `setValues()` enthält. Die `handleSubmit()`-Funktion gibt das `values`-Objekt in der Konsole aus, wenn das Formular abgeschickt wird. Die `input`-Elemente sind so eingerichtet, dass sie die Formularwerte mithilfe der `setValues()`-Funktion aktualisieren.

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
