# React useOnWindowScroll Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função executa uma função de callback toda vez que a janela é rolada. Para implementá-la:

1.  Use o hook `useRef()` para criar uma variável de referência, `listener`.
2.  Use o hook `useEffect()` e `EventTarget.addEventListener()` para ouvir o evento `'scroll'` do objeto `Window` e atribuir a referência do listener a `listener.current`.
3.  Use `EventTarget.removeEventListener()` para remover quaisquer listeners existentes quando o componente for desmontado.

Aqui está o código:

```jsx
const useOnWindowScroll = (callback) => {
  const listener = React.useRef(null);

  React.useEffect(() => {
    if (listener.current) {
      window.removeEventListener("scroll", listener.current);
    }
    listener.current = () => {
      callback(window.pageYOffset);
    };
    window.addEventListener("scroll", listener.current);
    return () => {
      window.removeEventListener("scroll", listener.current);
    };
  }, [callback]);
};
```

Para testar a função, você pode usá-la em um componente como este:

```jsx
const App = () => {
  useOnWindowScroll((scrollY) => console.log(`scroll Y: ${scrollY}`));
  return <p style={{ height: "300vh" }}>Scroll and check the console</p>;
};

ReactDOM.render(<App />, document.getElementById("root"));
```

Isso registrará a posição vertical da rolagem da janela toda vez que ela for rolada.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
