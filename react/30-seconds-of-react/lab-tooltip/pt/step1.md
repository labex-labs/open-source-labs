# _Tooltip_ (Dica de Ferramenta)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Aqui está uma versão mais clara, concisa e coerente do conteúdo:

---

Este código cria um componente de _tooltip_. Para usá-lo, faça o seguinte:

1. Use o _hook_ `useState()` para criar a variável `show` e defini-la como `false`.
2. Renderize um elemento contêiner que contém o elemento _tooltip_ e os `children` (filhos) passados para o componente.
3. Lide com os eventos `onMouseEnter` e `onMouseLeave` alternando a `className` do _tooltip_, que é controlada pela variável `show`.

Aqui está o código para o componente _tooltip_:

```css
.tooltip-container {
  position: relative;
}

.tooltip-box {
  position: absolute;
  top: calc(100% + 5px);
  display: none;
  padding: 5px;
  border-radius: 5px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
}

.tooltip-box.visible {
  display: block;
}

.tooltip-arrow {
  position: absolute;
  top: -10px;
  left: 50%;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgba(0, 0, 0, 0.7) transparent;
}
```

```jsx
const Tooltip = ({ children, text, ...rest }) => {
  const [show, setShow] = React.useState(false);

  return (
    <div className="tooltip-container">
      <div className={show ? "tooltip-box visible" : "tooltip-box"}>
        {text}
        <span className="tooltip-arrow" />
      </div>
      <div
        onMouseEnter={() => setShow(true)}
        onMouseLeave={() => setShow(false)}
        {...rest}
      >
        {children}
      </div>
    </div>
  );
};
```

Para usar o componente _tooltip_, chame `ReactDOM.createRoot()` com o seguinte código:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tooltip text="Simple tooltip">
    <button>Hover me!</button>
  </Tooltip>
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
