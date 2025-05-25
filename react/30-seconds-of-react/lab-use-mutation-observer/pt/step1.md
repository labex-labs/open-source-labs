# React useMutationObserver Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para observar as mudanças feitas na árvore DOM, o hook `useMutationObserver` pode ser usado. Veja como funciona:

1. O hook recebe três parâmetros: `ref`, `callback` e `options`.
2. Dentro do hook, um hook `useEffect()` é usado, que depende dos valores de `callback` e `options`.
3. Se a `ref` fornecida for inicializada, um novo `MutationObserver` é criado e recebe o `callback`.
4. `MutationObserver.observe()` é chamado com as `options` fornecidas para observar a `ref` fornecida em busca de mudanças.
5. `MutationObserver.disconnect()` é usado para remover o observador da `ref` quando o componente é desmontado.

Aqui está o código:

```jsx
const useMutationObserver = (
  ref,
  callback,
  options = {
    attributes: true,
    characterData: true,
    childList: true,
    subtree: true
  }
) => {
  React.useEffect(() => {
    if (!ref.current) return;

    const observer = new MutationObserver(callback);
    observer.observe(ref.current, options);

    return () => observer.disconnect();
  }, [callback, options, ref]);
};
```

No componente `App`, o hook `useMutationObserver` é usado para observar as mudanças feitas no elemento `mutationRef`. A função `incrementMutationCount` é passada como o `callback`.

```jsx
const App = () => {
  const mutationRef = React.useRef();
  const [mutationCount, setMutationCount] = React.useState(0);

  const incrementMutationCount = React.useCallback(() => {
    setMutationCount((count) => count + 1);
  }, []);

  useMutationObserver(mutationRef, incrementMutationCount);

  const [content, setContent] = React.useState("Hello world");

  return (
    <>
      <label htmlFor="content-input">Edite isso para atualizar o texto:</label>
      <textarea
        id="content-input"
        style={{ width: "100%" }}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div style={{ width: "100%" }} ref={mutationRef}>
        <div
          style={{
            resize: "both",
            overflow: "auto",
            maxWidth: "100%",
            border: "1px solid black"
          }}
        >
          <h2>Redimensione ou altere o conteúdo:</h2>
          <p>{content}</p>
        </div>
      </div>
      <div>
        <h3>Contagem de mutações {mutationCount}</h3>
      </div>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
