# Abas (Tabs)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para renderizar um componente de menu e visualização com abas, siga estas etapas:

1.  Defina um componente `Tabs`. Use o hook `useState()` para definir a variável de estado `bindIndex` para `defaultIndex`.
2.  Defina um componente `TabItem` e filtre os `children` passados para o componente `Tabs` para remover quaisquer nós desnecessários, exceto `TabItem`. Você pode fazer isso identificando o nome da função.
3.  Defina uma função chamada `changeTab`. Esta função será executada quando um usuário clicar em um `<button>` do menu.
4.  `changeTab` executa o callback passado, `onTabClick`, e atualiza `bindIndex` com base no elemento clicado.
5.  Use `Array.prototype.map()` nos nós coletados para renderizar o menu e a visualização das abas.
6.  Use o valor de `bindIndex` para determinar a aba ativa e aplicar a `className` correta.

Aqui está o código CSS para estilizar o menu e a visualização com abas:

```css
.tab-menu > button {
  cursor: pointer;
  padding: 8px 16px;
  border: 0;
  border-bottom: 2px solid transparent;
  background: none;
}

.tab-menu > button.focus {
  border-bottom: 2px solid #007bef;
}

.tab-menu > button:hover {
  border-bottom: 2px solid #007bef;
}

.tab-content {
  display: none;
}

.tab-content.selected {
  display: block;
}
```

Aqui está o código JavaScript para implementar o componente `Tabs`:

```jsx
const TabItem = (props) => <div {...props} />;

const Tabs = ({ defaultIndex = 0, onTabClick, children }) => {
  const [bindIndex, setBindIndex] = React.useState(defaultIndex);

  const changeTab = (newIndex) => {
    if (typeof onTabClick === "function") onTabClick(newIndex);
    setBindIndex(newIndex);
  };

  const items = children.filter((item) => item.type.name === "TabItem");

  return (
    <div className="wrapper">
      <div className="tab-menu">
        {items.map(({ props: { index, label } }) => (
          <button
            key={`tab-btn-${index}`}
            onClick={() => changeTab(index)}
            className={bindIndex === index ? "focus" : ""}
          >
            {label}
          </button>
        ))}
      </div>
      <div className="tab-view">
        {items.map(({ props }) => (
          <div
            {...props}
            className={`tab-content ${
              bindIndex === props.index ? "selected" : ""
            }`}
            key={`tab-content-${props.index}`}
          />
        ))}
      </div>
    </div>
  );
};
```

Finalmente, aqui está um exemplo de como usar o componente `Tabs`:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Tabs defaultIndex={1} onTabClick={console.log}>
    <TabItem label="A" index={1}>
      Lorem ipsum
    </TabItem>
    <TabItem label="B" index={2}>
      Dolor sit amet
    </TabItem>
  </Tabs>
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
