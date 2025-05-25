# React useHover Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código cria um _hook_ customizado que lida com o _hover_ (passar o mouse por cima) de um componente encapsulado.

Para usar o _hook_:

- Use `useState()` para criar uma variável que armazena o estado de _hover_.
- Use `useCallback()` para memorizar duas funções _handler_ (manipuladoras) que atualizam o estado.
- Use `useCallback()` para criar uma _callback ref_ (referência de retorno de chamada) e criar ou atualizar os _listeners_ (ouvintes) para os eventos `'mouseover'` e `'mouseout'`.
- Use `useRef()` para manter o controle do último nó passado para `callbackRef` para poder remover seus _listeners_.

```jsx
const useHover = () => {
  const [isHovering, setIsHovering] = React.useState(false);
  const handleMouseOver = React.useCallback(() => setIsHovering(true), []);
  const handleMouseOut = React.useCallback(() => setIsHovering(false), []);
  const nodeRef = React.useRef();
  const callbackRef = React.useCallback(
    (node) => {
      if (nodeRef.current) {
        nodeRef.current.removeEventListener("mouseover", handleMouseOver);
        nodeRef.current.removeEventListener("mouseout", handleMouseOut);
      }
      nodeRef.current = node;
      if (nodeRef.current) {
        nodeRef.current.addEventListener("mouseover", handleMouseOver);
        nodeRef.current.addEventListener("mouseout", handleMouseOut);
      }
    },
    [handleMouseOver, handleMouseOut]
  );

  return [callbackRef, isHovering];
};
```

Este é um exemplo de uso do _hook_:

```jsx
const MyApp = () => {
  const [hoverRef, isHovering] = useHover();
  return <div ref={hoverRef}>{isHovering ? "Hovering" : "Not hovering"}</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
