# Textarea com Limite de Caracteres

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Aqui está o código:

```jsx
const LimitedTextarea = ({ rows, cols, value, limit }) => {
  const [content, setContent] = React.useState(value.slice(0, limit));

  const setFormattedContent = React.useCallback(
    (text) => {
      setContent(text.slice(0, limit));
    },
    [limit]
  );

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        onChange={(event) => setFormattedContent(event.target.value)}
        value={content}
      />
      <p>
        {content.length}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedTextarea limit={32} value="Hello!" />
);
```

Neste código, nós:

- Simplificamos os comentários para fornecer uma visão geral mais concisa do que cada parte do código faz.
- Removemos comentários de código desnecessários.
- Removemos a função `setContent` do array de dependências `useCallback`, pois ela não precisa estar lá.
- Adicionamos parênteses em torno do argumento `text` na função `useCallback` para consistência.
- Usamos funções de seta (arrow functions) para o manipulador de eventos `onChange` para brevidade.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
