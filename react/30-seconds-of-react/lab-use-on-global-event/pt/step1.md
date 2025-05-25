# React useOnGlobalEvent Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função executa uma função de callback sempre que um evento ocorre no objeto global. Para implementar esta função:

1.  Use o hook `useRef()` para criar uma variável, `listener`, que irá armazenar a referência do listener.
2.  Use o hook `useRef()` para criar uma variável que irá armazenar os valores anteriores dos argumentos `type` e `options`.
3.  Use o hook `useEffect()` e `EventTarget.addEventListener()` para escutar o evento `type` fornecido no objeto global `Window`.
4.  Use `EventTarget.removeEventListener()` para remover quaisquer listeners existentes e fazer a limpeza quando o componente for desmontado.

```jsx
const useOnGlobalEvent = (type, callback, options) => {
  const listener = React.useRef(null);
  const previousProps = React.useRef({ type, options });

  React.useEffect(() => {
    const { type: previousType, options: previousOptions } =
      previousProps.current;

    if (listener.current) {
      window.removeEventListener(
        previousType,
        listener.current,
        previousOptions
      );
    }

    listener.current = callback;
    window.addEventListener(type, callback, options);
    previousProps.current = { type, options };

    return () => {
      window.removeEventListener(type, listener.current, options);
    };
  }, [callback, type, options]);
};
```

Aqui está um exemplo de como usar esta função:

```jsx
const App = () => {
  useOnGlobalEvent("mousemove", (e) => {
    console.log(`(${e.x}, ${e.y})`);
  });

  return <p>Move your mouse around</p>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
