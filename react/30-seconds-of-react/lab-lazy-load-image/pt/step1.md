# Carregamento Lento de Imagens (Lazy-Loading Image)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para renderizar uma imagem que suporte carregamento lento, siga estes passos:

1.  Use o hook `useState()` para criar um valor com estado que indica se a imagem foi carregada.
2.  Use o hook `useEffect()` para verificar se o `HTMLImageElement.prototype` contém `'loading'`. Isso verifica se o carregamento lento é suportado nativamente. Caso contrário, crie um novo `IntersectionObserver` e use `IntersectionObserver.observer()` para observar o elemento `<img>`. Use o valor de `return` do hook para limpar quando o componente for desmontado.
3.  Use o hook `useCallback()` para memorizar uma função de callback para o `IntersectionObserver`. Este callback atualizará a variável de estado `isLoaded` e usará `IntersectionObserver.disconnect()` para desconectar a instância do `IntersectionObserver`.
4.  Use o hook `useRef()` para criar duas refs. Uma manterá o elemento `<img>` e a outra a instância do `IntersectionObserver`, se necessário.
5.  Finalmente, renderize o elemento `<img>` com os atributos fornecidos. Aplique `loading='lazy'` para fazê-lo carregar lentamente, se necessário. Use `isLoaded` para determinar o valor do atributo `src`.

Aqui está um exemplo de implementação desses passos:

```jsx
const LazyLoadImage = ({
  alt,
  src,
  className,
  loadInitially = false,
  observerOptions = { root: null, rootMargin: "200px 0px" },
  ...props
}) => {
  const observerRef = React.useRef(null);
  const imgRef = React.useRef(null);
  const [isLoaded, setIsLoaded] = React.useState(loadInitially);

  const observerCallback = React.useCallback(
    (entries) => {
      if (entries[0].isIntersecting) {
        observerRef.current.disconnect();
        setIsLoaded(true);
      }
    },
    [observerRef]
  );

  React.useEffect(() => {
    if (loadInitially) return;

    if ("loading" in HTMLImageElement.prototype) {
      setIsLoaded(true);
      return;
    }

    observerRef.current = new IntersectionObserver(
      observerCallback,
      observerOptions
    );
    observerRef.current.observe(imgRef.current);
    return () => {
      observerRef.current.disconnect();
    };
  }, []);

  return (
    <img
      alt={alt}
      src={isLoaded ? src : ""}
      ref={imgRef}
      className={className}
      loading={loadInitially ? undefined : "lazy"}
      {...props}
    />
  );
};
```

Para usar este componente `LazyLoadImage`, basta chamá-lo com os atributos `src` e `alt` da imagem:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <LazyLoadImage
    src="https://picsum.photos/id/1080/600/600"
    alt="Strawberries"
  />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
