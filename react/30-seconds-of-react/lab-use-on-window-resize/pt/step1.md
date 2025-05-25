# Hook React useOnWindowResize

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código executa uma função de callback toda vez que a janela é redimensionada. Para implementá-lo, você deve seguir estes passos:

1. Crie uma variável chamada `listener` usando o hook `useRef()`. Esta variável armazenará a referência ao listener.

2. Use o hook `useEffect()` e `EventTarget.addEventListener()` para escutar o evento `'resize'` do objeto global `Window`. Quando o evento for acionado, chame a função `callback`.

3. Faça a limpeza removendo quaisquer listeners existentes com `EventTarget.removeEventListener()` quando o componente for desmontado.

Aqui está o código:

```jsx
const useOnWindowResize = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("resize", listener.current);
    }
    listener.current = callback;
    window.addEventListener("resize", callback);
    return () => {
      window.removeEventListener("resize", callback);
    };
  }, [callback]);
};

const App = () => {
  useOnWindowResize(() =>
    console.log(`Window size: (${window.innerWidth}, ${window.innerHeight})`)
  );
  return <p>Resize the window and check the console.</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
