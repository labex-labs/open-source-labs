# Vista de árbol de objetos expandible

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

El siguiente código renderiza una vista de árbol collapsible de un objeto JSON o matriz. Al usar el hook `useState()` para crear la variable de estado `isToggled`, se puede determinar el estado inicial del contenido (colapsado/expandido) al pasar la propiedad `toggled`. La apariencia del componente se determina en función de `isParentToggled`, `isToggled`, `name` y verificando `Array.isArray()` en `data`.

Para cada hijo en `data`, determinar si es un objeto o matriz y renderizar recursivamente un sub-árbol o un elemento de texto con el estilo adecuado. Para alternar el estado del componente, renderizar un elemento `<span>` y enlazar su evento `onClick` para alterar el estado `isToggled` del componente.

Los estilos CSS se definen para la apariencia del componente, incluyendo las propiedades `margin`, `position`, `border` y `display`.

```jsx
const TreeView = ({
  data,
  toggled = true,
  name = null,
  isLast = true,
  isChildElement = false,
  isParentToggled = true
}) => {
  const [isToggled, setIsToggled] = React.useState(toggled);
  const isDataArray = Array.isArray(data);

  return (
    <div
      className={`tree-element ${isParentToggled && "collapsed"} ${
        isChildElement && "is-child"
      }`}
    >
      <span
        className={isToggled ? "toggler" : "toggler closed"}
        onClick={() => setIsToggled(!isToggled)}
      />
      {name ? <strong>&nbsp;&nbsp;{name}: </strong> : <span>&nbsp;&nbsp;</span>}
      {isDataArray ? "[" : "{"}
      {!isToggled && "..."}
      {Object.keys(data).map((v, i, a) =>
        typeof data[v] === "object" ? (
          <TreeView
            key={`${name}-${v}-${i}`}
            data={data[v]}
            isLast={i === a.length - 1}
            name={isDataArray ? null : v}
            isChildElement
            isParentToggled={isParentToggled && isToggled}
          />
        ) : (
          <p
            key={`${name}-${v}-${i}`}
            className={isToggled ? "tree-element" : "tree-element collapsed"}
          >
            {isDataArray ? "" : <strong>{v}: </strong>}
            {data[v]}
            {i === a.length - 1 ? "" : ","}
          </p>
        )
      )}
      {isDataArray ? "]" : "}"}
      {!isLast ? "," : ""}
    </div>
  );
};
```

```css
.tree-element {
  margin: 0 0 0 4px;
  position: relative;
}

.tree-element.is-child {
  margin-left: 16px;
}

div.tree-element::before {
  content: "";
  position: absolute;
  top: 24px;
  left: 1px;
  height: calc(100% - 48px);
  border-left: 1px solid gray;
}

p.tree-element {
  margin-left: 16px;
}

.toggler {
  position: absolute;
  top: 10px;
  left: 0px;
  width: 0;
  height: 0;
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-left: 5px solid gray;
  cursor: pointer;
}

.toggler.closed {
  transform: rotate(90deg);
}

.collapsed {
  display: none;
}
```

```jsx
const data = {
  lorem: {
    ipsum: "dolor sit",
    amet: {
      consectetur: "adipiscing",
      elit: [
        "duis",
        "vitae",
        {
          semper: "orci"
        },
        {
          est: "sed ornare"
        },
        "etiam",
        ["laoreet", "tincidunt"],
        ["vestibulum", "ante"]
      ]
    },
    ipsum: "primis"
  }
};
ReactDOM.createRoot(document.getElementById("root")).render(
  <TreeView data={data} name="data" />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
