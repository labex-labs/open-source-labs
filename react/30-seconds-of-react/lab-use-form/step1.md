# React useForm Hook

> `index.html` and `script.js` have already been provided in the VM. In general, you only need to add code to `script.js` and `style.css`.

To create a stateful value from the fields in a form, you can use the `useState()` hook to create a state variable for the values in the form. Then, create a function that updates the state variable based on the appropriate event triggered by a form field.

Here's an example implementation:

```jsx
const useForm = (initialValues) => {
  const [values, setValues] = React.useState(initialValues);

  return [
    values,
    (e) => {
      setValues({
        ...values,
        [e.target.name]: e.target.value,
      });
    },
  ];
};
```

In the example above, `useForm()` takes an initial state object, creates a state variable `values` using `useState()`, and returns an array with `values` and a function that updates `values` based on the event passed to it.

You can use `useForm()` in a form component like this:

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

In the `Form` component, `useForm()` is called with an initial state object and returns an array with `values` and `setValues()`. The `handleSubmit()` function logs the `values` object to the console when the form is submitted. The `input` elements are set up to update the form values using the `setValues()` function.

Please click on 'Go Live' in the bottom right corner to run the web service on port 8080. Then, you can refresh the HTTP 8080 Tab to preview the web page.
