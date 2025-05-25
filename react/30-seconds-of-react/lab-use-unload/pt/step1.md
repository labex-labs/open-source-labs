# React useUnload Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

O evento `beforeunload` da janela pode ser tratado usando as seguintes etapas:

1. Crie uma ref para a função de callback, `fn`, usando o hook `useRef()`.
2. Use o hook `useEffect()` e `EventTarget.addEventListener()` para lidar com o evento `'beforeunload'`, que é acionado quando o usuário está prestes a fechar a janela.
3. Use `EventTarget.removeEventListener()` para realizar a limpeza após o componente ser desmontado.

Aqui está o código:

```jsx
const useUnload = (fn) => {
  const callbackRef = React.useRef(fn);

  React.useEffect(() => {
    const callback = callbackRef.current;
    window.addEventListener("beforeunload", callback);
    return () => {
      window.removeEventListener("beforeunload", callback);
    };
  }, [callbackRef]);
};

const App = () => {
  useUnload((e) => {
    e.preventDefault();
    const exit = confirm("Are you sure you want to leave?");
    if (exit) window.close();
  });

  return <div>Try closing the window.</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
