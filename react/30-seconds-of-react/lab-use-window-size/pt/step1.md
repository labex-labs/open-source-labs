# React useWindowSize Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para rastrear as dimensões da janela do navegador, as seguintes etapas podem ser tomadas:

1. Use o hook `useState()` para inicializar uma variável de estado `windowSize` que conterá as dimensões da janela. Inicialize com ambos os valores definidos como `undefined` para evitar incompatibilidade entre as renderizações do servidor e do cliente.

```jsx
const [windowSize, setWindowSize] = React.useState({
  width: undefined,
  height: undefined
});
```

2. Crie uma função `handleResize()` que usa `Window.innerWidth` e `Window.innerHeight` para atualizar a variável de estado. Esta função será chamada sempre que o evento `'resize'` for acionado.

```jsx
const handleResize = () =>
  setWindowSize({ width: window.innerWidth, height: window.innerHeight });
```

3. Use o hook `useEffect()` para definir um listener apropriado para o evento `'resize'` no momento da montagem e limpá-lo no momento da desmontagem.

```jsx
React.useEffect(() => {
  window.addEventListener("resize", handleResize);

  handleResize();

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

Juntando tudo, o custom hook `useWindowSize()` pode ser definido da seguinte forma:

```jsx
const useWindowSize = () => {
  const [windowSize, setWindowSize] = React.useState({
    width: undefined,
    height: undefined
  });

  const handleResize = () =>
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });

  React.useEffect(() => {
    window.addEventListener("resize", handleResize);

    handleResize();

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return windowSize;
};
```

Para usar o hook `useWindowSize()`, basta chamá-lo em um componente e desestruturar os valores `width` e `height` do objeto retornado.

```jsx
const MyApp = () => {
  const { width, height } = useWindowSize();

  return (
    <p>
      Window size: ({width} x {height})
    </p>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
