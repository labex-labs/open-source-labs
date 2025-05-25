# React useSSR Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para verificar se o código está sendo executado em um navegador ou servidor, crie um hook personalizado que usa `typeof`, `Window`, `Window.document` e `Document.createElement()` para determinar se o DOM está disponível. Use o hook `useState()` para definir a variável de estado `inBrowser` e o hook `useEffect()` para atualizá-la e limpar no final. Use o hook `useMemo()` para memorizar os valores de retorno do hook personalizado.

Aqui está o código:

```jsx
const isDOMavailable = !!(
  typeof window !== "undefined" &&
  window.document &&
  window.document.createElement
);

const useSSR = () => {
  const [inBrowser, setInBrowser] = React.useState(isDOMavailable);

  React.useEffect(() => {
    setInBrowser(isDOMavailable);
    return () => {
      setInBrowser(false);
    };
  }, []);

  const useSSRObject = React.useMemo(
    () => ({
      isBrowser: inBrowser,
      isServer: !inBrowser,
      canUseWorkers: typeof Worker !== "undefined",
      canUseEventListeners: inBrowser && !!window.addEventListener,
      canUseViewport: inBrowser && !!window.screen
    }),
    [inBrowser]
  );

  return useSSRObject;
};

const SSRChecker = (props) => {
  const { isBrowser, isServer } = useSSR();

  return <p>{isBrowser ? "Running on browser" : "Running on server"}</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<SSRChecker />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
