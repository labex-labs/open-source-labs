# React useIntersectionObserver Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para observar as mudanças de visibilidade de um determinado elemento, siga estes passos:

1. Use o hook `useState()` para armazenar o valor de interseção do elemento fornecido.
2. Crie um `IntersectionObserver` com as `options` fornecidas e um callback apropriado para atualizar a variável de estado `isIntersecting`.
3. Use o hook `useEffect()` para chamar `IntersectionObserver.observe()` ao montar o componente e limpar usando `IntersectionObserver.unobserve()` ao desmontar.

Aqui está um exemplo de implementação:

```jsx
const useIntersectionObserver = (ref, options) => {
  const [isIntersecting, setIsIntersecting] = React.useState(false);

  React.useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    }, options);

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      observer.unobserve(ref.current);
    };
  }, [ref, options]);

  return isIntersecting;
};
```

Você pode usar o hook `useIntersectionObserver` assim:

```jsx
const MyApp = () => {
  const ref = React.useRef();
  const onScreen = useIntersectionObserver(ref, { threshold: 0.5 });

  return (
    <div>
      <div style={{ height: "100vh" }}>Scroll down</div>
      <div style={{ height: "100vh" }} ref={ref}>
        <p>{onScreen ? "Element is on screen." : "Scroll more!"}</p>
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
