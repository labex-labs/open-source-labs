# Acordeão Recolhível (Collapsible Accordion)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para renderizar um menu acordeão com múltiplos elementos de conteúdo recolhíveis, você pode seguir estes passos:

1.  Defina um componente `AccordionItem` que renderiza um `<button>` e atualiza o componente enquanto notifica seu pai via o callback `handleClick`.
2.  Use a prop `isCollapsed` em `AccordionItem` para determinar sua aparência e definir seu `className`.
3.  Defina um componente `Accordion` e use o hook `useState()` para inicializar o valor da variável de estado `bindIndex` para `defaultIndex`.
4.  Filtre `children` para remover nós desnecessários, exceto para `AccordionItem`, identificando o nome da função.
5.  Use `Array.prototype.map()` nos nós coletados para renderizar os elementos recolhíveis individuais.
6.  Defina `changeItem`, que será executado ao clicar no `<button>` de um `AccordionItem`.
7.  `changeItem` executa o callback passado, `onItemClick`, e atualiza `bindIndex` com base no elemento clicado.

Aqui está o código:

```css
.accordion-item.collapsed {
  display: none;
}

.accordion-item.expanded {
  display: block;
}

.accordion-button {
  display: block;
  width: 100%;
}
```

```jsx
const AccordionItem = ({ label, isCollapsed, handleClick, children }) => {
  return (
    <>
      <button className="accordion-button" onClick={handleClick}>
        {label}
      </button>
      <div
        className={`accordion-item ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};

const Accordion = ({ defaultIndex, onItemClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeItem = (itemIndex) => {
    if (typeof onItemClick === "function") onItemClick(itemIndex);
    if (itemIndex !== bindIndex) setBindIndex(itemIndex);
  };

  const items = children.filter((item) => item.type.name === "AccordionItem");

  return (
    <>
      {items.map(({ props }) => (
        <AccordionItem
          isCollapsed={bindIndex !== props.index}
          label={props.label}
          handleClick={() => changeItem(props.index)}
          children={props.children}
        />
      ))}
    </>
  );
};
```

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Accordion defaultIndex="1" onItemClick={console.log}>
    <AccordionItem label="A" index="1">
      Lorem ipsum
    </AccordionItem>
    <AccordionItem label="B" index="2">
      Dolor sit amet
    </AccordionItem>
  </Accordion>
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
