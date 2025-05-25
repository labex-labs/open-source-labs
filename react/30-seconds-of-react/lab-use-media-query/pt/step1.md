# React useMediaQuery Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função verifica se o ambiente atual corresponde a uma determinada media query (consulta de mídia) e retorna o valor apropriado.

- Primeiro, verifique se `Window` e `Window.matchMedia()` existem. Caso contrário (por exemplo, em um ambiente SSR ou navegador não suportado), retorne `whenFalse`.
- Use `Window.matchMedia()` para corresponder à `query` fornecida. Converta sua propriedade `matches` para um booleano e armazene-a em uma variável de estado, `match`, usando o hook `useState()`.
- Use o hook `useEffect()` para adicionar um listener (ouvinte) para mudanças e para limpar os listeners após a destruição do hook.
- Finalmente, retorne `whenTrue` ou `whenFalse` com base no valor de `match`.

```jsx
const useMediaQuery = (query, whenTrue, whenFalse) => {
  if (
    typeof window === "undefined" ||
    typeof window.matchMedia === "undefined"
  ) {
    return whenFalse;
  }

  const mediaQuery = window.matchMedia(query);
  const [match, setMatch] = React.useState(!!mediaQuery.matches);

  React.useEffect(() => {
    const handler = () => setMatch(!!mediaQuery.matches);
    mediaQuery.addListener(handler);
    return () => mediaQuery.removeListener(handler);
  }, [mediaQuery]);

  return match ? whenTrue : whenFalse;
};
```

```jsx
const ResponsiveText = () => {
  const text = useMediaQuery(
    "(max-width: 400px)",
    "Less than 400px wide",
    "More than 400px wide"
  );

  return <span>{text}</span>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ResponsiveText />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
