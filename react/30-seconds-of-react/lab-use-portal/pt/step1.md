# React usePortal Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para criar um portal que renderiza filhos fora do componente pai, siga estes passos:

1.  Use o hook `useState()` para criar uma variável de estado que armazena as funções `render()` e `remove()` para o portal.
2.  Use `ReactDOM.createPortal()` e `ReactDOM.unmountComponentAtNode()` para criar um portal e uma função para removê-lo. Use o hook `useCallback()` para encapsular e memorizar essas funções como `createPortal()`.
3.  Use o hook `useEffect()` para chamar `createPortal()` e atualizar a variável de estado sempre que o valor de `el` mudar.
4.  Finalmente, retorne a função `render()` da variável de estado.

Aqui está um exemplo de implementação:

```jsx
const usePortal = (el) => {
  const [portal, setPortal] = React.useState({
    render: () => null,
    remove: () => null
  });

  const createPortal = React.useCallback((el) => {
    const Portal = ({ children }) => ReactDOM.createPortal(children, el);
    const remove = () => ReactDOM.unmountComponentAtNode(el);
    return { render: Portal, remove };
  }, []);

  React.useEffect(() => {
    if (el) portal.remove();
    const newPortal = createPortal(el);
    setPortal(newPortal);
    return () => newPortal.remove(el);
  }, [el]);

  return portal.render;
};
```

Para usar este hook, crie um componente que chama `usePortal()` com o elemento DOM desejado como argumento. Este componente pode então usar a função `render()` retornada para renderizar conteúdo no portal:

```jsx
const App = () => {
  const Portal = usePortal(document.querySelector("title"));

  return (
    <p>
      Hello world!
      <Portal>Portalized Title</Portal>
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
