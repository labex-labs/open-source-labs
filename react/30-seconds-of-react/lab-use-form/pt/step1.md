# React useForm Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para criar um valor com estado a partir dos campos em um formulário, você pode usar o hook `useState()` para criar uma variável de estado para os valores no formulário. Em seguida, crie uma função que atualize a variável de estado com base no evento apropriado acionado por um campo do formulário.

Aqui está um exemplo de implementação:

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

No exemplo acima, `useForm()` recebe um objeto de estado inicial, cria uma variável de estado `values` usando `useState()` e retorna um array com `values` e uma função que atualiza `values` com base no evento passado para ela.

Você pode usar `useForm()` em um componente de formulário assim:

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

No componente `Form`, `useForm()` é chamado com um objeto de estado inicial e retorna um array com `values` e `setValues()`. A função `handleSubmit()` registra o objeto `values` no console quando o formulário é enviado. Os elementos `input` são configurados para atualizar os valores do formulário usando a função `setValues()`.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
