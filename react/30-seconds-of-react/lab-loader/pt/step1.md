# Carregador Giratório (Spinning Loader)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

**Renderiza um componente de carregamento giratório.**

Para renderizar um componente de carregamento giratório, siga estas etapas:

1.  Renderize um elemento SVG cujas dimensões são determinadas pela prop `size`.
2.  Use CSS para animar o SVG, criando uma animação giratória. Especificamente, adicione a classe `.loader` ao SVG e defina a propriedade `animation` como `rotate 2s linear infinite`. Além disso, defina os keyframes `rotate` com uma propriedade `transform` que gira o SVG em 360 graus.
3.  Adicione um elemento `circle` ao SVG, que representa o círculo giratório. Para animar o círculo, adicione o seletor `.loader circle` e defina a propriedade `animation` como `dash 1.5s ease-in-out infinite`. Além disso, defina os keyframes `dash` com as propriedades `stroke-dasharray` e `stroke-dashoffset` que criam um padrão de traço tracejado que se move ao redor do círculo.
4.  Finalmente, crie um componente `Loader` que renderiza o SVG com a prop `size` passada como os atributos width e height.

```css
.loader {
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  100% {
    transform: rotate(360deg);
  }
}

.loader circle {
  animation: dash 1.5s ease-in-out infinite;
}

@keyframes dash {
  0% {
    stroke-dasharray: 1, 150;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -35;
  }
  100% {
    stroke-dasharray: 90, 150;
    stroke-dashoffset: -124;
  }
}
```

```jsx
const Loader = ({ size }) => {
  return (
    <svg
      className="loader"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
    </svg>
  );
};
```

Para usar o componente `Loader` com um tamanho de 24, chame `ReactDOM.createRoot(document.getElementById('root')).render(<Loader size={24} />);`.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
