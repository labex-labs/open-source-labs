# Campo de Entrada Controlado

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este trecho de código fornece um elemento `<input>` controlado que utiliza uma função de callback para informar seu pai sobre quaisquer atualizações em seu valor. Veja como funciona:

- O valor do campo de entrada controlado é determinado pela prop `value` passada do pai.
- Quaisquer alterações feitas no campo de entrada pelo usuário são capturadas pelo evento `onChange`, que aciona a função de callback `onValueChange` e envia o novo valor de volta para o componente pai.
- Para atualizar o valor do campo de entrada, o pai deve atualizar a prop `value` que ele passa para o componente de entrada controlado.

Aqui está um exemplo de implementação do componente `ControlledInput`, seguido por um exemplo de uso em um componente `Form`:

```jsx
const ControlledInput = ({ value, onValueChange, ...rest }) => {
  return (
    <input
      value={value}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

const Form = () => {
  const [value, setValue] = React.useState("");

  return (
    <ControlledInput
      type="text"
      placeholder="Insert some text here..."
      value={value}
      onValueChange={setValue}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
