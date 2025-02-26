# React useForm Hook

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para crear un valor con estado a partir de los campos de un formulario, puedes usar el hook `useState()` para crear una variable de estado para los valores en el formulario. Luego, crea una función que actualice la variable de estado en función del evento adecuado desencadenado por un campo de formulario.

A continuación, se muestra una implementación de ejemplo:

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

En el ejemplo anterior, `useForm()` toma un objeto de estado inicial, crea una variable de estado `values` usando `useState()` y devuelve un array con `values` y una función que actualiza `values` en función del evento que se le pasa.

Puedes usar `useForm()` en un componente de formulario de la siguiente manera:

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

En el componente `Form`, `useForm()` se llama con un objeto de estado inicial y devuelve un array con `values` y `setValues()`. La función `handleSubmit()` registra el objeto `values` en la consola cuando se envía el formulario. Los elementos `input` se configuran para actualizar los valores del formulario usando la función `setValues()`.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
