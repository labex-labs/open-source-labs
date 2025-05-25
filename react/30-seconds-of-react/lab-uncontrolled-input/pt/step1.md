# Campo de Entrada Não Controlado

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código renderiza um elemento `<input>` não controlado que usa uma função de callback para informar seu pai sobre as atualizações de valor. Para usá-lo:

- Passe o valor inicial do pai usando a prop `defaultValue`.
- Passe uma função de callback chamada `onValueChange` para lidar com as atualizações de valor.
- Use o evento `onChange` para disparar o callback e enviar o novo valor para o pai.

Aqui está um exemplo:

```jsx
const UncontrolledInput = ({ defaultValue, onValueChange, ...rest }) => {
  return (
    <input
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <UncontrolledInput
    type="text"
    placeholder="Insert some text here..."
    onValueChange={console.log}
  />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
