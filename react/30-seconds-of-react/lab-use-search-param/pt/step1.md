# Hook React useSearchParam

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para rastrear o parâmetro de pesquisa da localização do navegador, use as seguintes etapas:

1.  Crie um callback usando o hook `useCallback()`. O callback deve usar o construtor `URLSearchParams` para obter o valor atual do parâmetro desejado.

```jsx
const getValue = React.useCallback(
  () => new URLSearchParams(window.location.search).get(param),
  [param]
);
```

2.  Crie uma variável de estado que armazena o valor atual do parâmetro usando o hook `useState()`.

```jsx
const [value, setValue] = React.useState(getValue);
```

3.  Defina os ouvintes de eventos apropriados para atualizar a variável de estado ao montar e limpe-os ao desmontar usando o hook `useEffect()`.

```jsx
React.useEffect(() => {
  const onChange = () => {
    setValue(getValue());
  };

  window.addEventListener("popstate", onChange);
  window.addEventListener("pushstate", onChange);
  window.addEventListener("replacestate", onChange);

  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener("pushstate", onChange);
    window.removeEventListener("replacestate", onChange);
  };
}, []);
```

Aqui está um exemplo de como usar este hook personalizado em um componente:

```jsx
const MyApp = () => {
  const post = useSearchParam("post");

  return (
    <>
      <p>Valor do parâmetro post: {post || "null"}</p>
      <button
        onClick={() =>
          history.pushState({}, "", location.pathname + "?post=42")
        }
      >
        Ver post 42
      </button>
      <button onClick={() => history.pushState({}, "", location.pathname)}>
        Sair
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Este exemplo cria um componente `MyApp` que usa o hook personalizado `useSearchParam` para rastrear o valor do parâmetro `post` na pesquisa de localização. O valor de `post` é exibido em uma tag de parágrafo. Dois botões também estão incluídos para demonstrar como alterar o valor do parâmetro de pesquisa de localização.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
