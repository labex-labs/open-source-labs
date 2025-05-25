# Elemento Textarea Não Controlado

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função renderiza um elemento `<textarea>` que não é controlado pelo componente pai. Ela usa uma função de callback para passar o valor da entrada para o componente pai.

Para usar esta função:

- Passe a propriedade `defaultValue` do componente pai como o valor inicial do campo de entrada.
- Use o evento `onChange` para acionar o callback `onValueChange` e enviar o novo valor para o pai.

```jsx
const TextArea = ({
  cols = 20,
  rows = 2,
  defaultValue,
  onValueChange,
  ...rest
}) => {
  return (
    <textarea
      cols={cols}
      rows={rows}
      defaultValue={defaultValue}
      onChange={({ target: { value } }) => onValueChange(value)}
      {...rest}
    />
  );
};
```

Exemplo de uso:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <TextArea
    placeholder="Insert some text here..."
    onValueChange={(val) => console.log(val)}
  />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
