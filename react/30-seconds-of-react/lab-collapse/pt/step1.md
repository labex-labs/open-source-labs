# Conteúdo Recolhível

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Esta função renderiza um componente recolhível com um botão que alterna a visibilidade de seu conteúdo. Veja como usá-lo:

1. Use o hook `useState()` para criar a variável de estado `isCollapsed`, que representa se o conteúdo está atualmente recolhido ou expandido. Inicialize-a como `collapsed`.
2. Use o elemento `<button>` para alternar o estado `isCollapsed` e mostrar/ocultar o conteúdo passado via a prop `children`.
3. Use `isCollapsed` para aplicar a classe CSS apropriada ao contêiner de conteúdo, seja `collapsed` ou `expanded`, o que determina sua aparência.
4. Atualize o atributo `aria-expanded` do contêiner de conteúdo com base no estado `isCollapsed`, para tornar o componente acessível a usuários com deficiências.

Aqui está o código CSS necessário para este componente:

```css
.collapse-button {
  display: block;
  width: 100%;
}

.collapse-content.collapsed {
  display: none;
}

.collapse-content.expanded {
  display: block;
}
```

E aqui está o código JavaScript:

```jsx
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? "Show" : "Hide"} content
      </button>
      <div
        className={`collapse-content ${isCollapsed ? "collapsed" : "expanded"}`}
        aria-expanded={isCollapsed}
      >
        {children}
      </div>
    </>
  );
};
```

Para usar este componente, basta chamá-lo com o conteúdo que você deseja recolher:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Collapse>
    <h1>This is a collapse</h1>
    <p>Hello world!</p>
  </Collapse>
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
