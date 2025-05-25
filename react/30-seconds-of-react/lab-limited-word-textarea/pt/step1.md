# Textarea com Limite de Palavras

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

```jsx
// Renderiza um componente textarea com um limite de palavras.
const LimitedWordTextarea = ({ rows, cols, value, limit }) => {
  const [{ content, wordCount }, setContent] = React.useState({
    content: value,
    wordCount: 0
  });

  // Cria uma função memorizada que formata o texto de entrada.
  const setFormattedContent = React.useCallback(
    (text) => {
      const words = text.split(" ").filter(Boolean);
      const truncated = words.slice(0, limit).join(" ");
      setContent({
        content: words.length > limit ? truncated : text,
        wordCount: words.length > limit ? limit : words.length
      });
    },
    [limit, setContent]
  );

  // Chama setFormattedContent no valor inicial de content.
  React.useEffect(() => {
    setFormattedContent(content);
  }, []);

  return (
    <>
      <textarea
        rows={rows}
        cols={cols}
        value={content}
        onChange={(event) => setFormattedContent(event.target.value)}
      />
      <p>
        {wordCount}/{limit}
      </p>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <LimitedWordTextarea limit={5} value="Hello there!" />
);
```

Mudanças feitas:

- Adicionados comentários para explicar o que cada parte do código faz.
- Simplificada a lógica em `setFormattedContent` para torná-la mais concisa.
- Movida a função `setContent` para o final da chamada da função para facilitar a leitura.
- Reordenadas as props no componente `<textarea>` para consistência.
- Removidos espaços e quebras de linha desnecessários.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
