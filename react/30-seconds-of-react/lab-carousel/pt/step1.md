# Carousel (Carrossel)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código renderiza um componente carousel (carrossel). Aqui estão as etapas que ele executa:

1. Ele usa o hook `useState()` para criar a variável de estado `active` e a inicializa com `0` (o índice do primeiro item no carousel).
2. Ele usa o hook `useEffect()` para configurar um timer com `setTimeout()`. Quando o timer dispara, ele atualiza o valor de `active` para o índice do próximo item no carousel (usando o operador módulo para voltar ao início, se necessário). Ele também limpa o timer quando o componente é desmontado.
3. Ele calcula o `className` para cada item do carousel mapeando-os e aplicando a classe apropriada com base em se o item está atualmente ativo ou não.
4. Ele renderiza os itens do carousel usando `React.cloneElement()`, passando quaisquer props adicionais usando `...rest` e adicionando o `className` calculado a cada item.

Os estilos CSS definem o layout do carousel e seus itens. O container do carousel tem `position: relative`, enquanto os itens têm `position: absolute` e `visibility: hidden` por padrão. Quando um item está ativo, ele recebe uma classe `visible`, que define sua `visibility` como `visible`.

```css
.carousel {
  position: relative;
}

.carousel-item {
  position: absolute;
  visibility: hidden;
}

.carousel-item.visible {
  visibility: visible;
}
```

Aqui está o código completo:

```jsx
const Carousel = ({ carouselItems, ...rest }) => {
  const [active, setActive] = React.useState(0);
  let scrollInterval = null;

  React.useEffect(() => {
    scrollInterval = setTimeout(() => {
      setActive((active + 1) % carouselItems.length);
    }, 2000);
    return () => clearTimeout(scrollInterval);
  });

  return (
    <div className="carousel">
      {carouselItems.map((item, index) => {
        const activeClass = active === index ? " visible" : "";
        return React.cloneElement(item, {
          ...rest,
          className: `carousel-item${activeClass}`
        });
      })}
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <Carousel
    carouselItems={[
      <div>carousel item 1</div>,
      <div>carousel item 2</div>,
      <div>carousel item 3</div>
    ]}
  />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
