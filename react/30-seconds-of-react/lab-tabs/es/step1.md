# Tabs

> `index.html` y `script.js` ya se han proporcionado en la VM. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para renderizar un menú y un componente de vista con pestañas, siga estos pasos:

1. Defina un componente `Tabs`. Utilice el hook `useState()` para establecer la variable de estado `bindIndex` en `defaultIndex`.
2. Defina un componente `TabItem` y filtre los `children` pasados al componente `Tabs` para eliminar cualquier nodo no necesario excepto `TabItem`. Puede hacer esto identificando el nombre de la función.
3. Defina una función llamada `changeTab`. Esta función se ejecutará cuando un usuario haga clic en un `<button>` del menú.
4. `changeTab` ejecuta la devolución de llamada pasada, `onTabClick`, y actualiza `bindIndex` según el elemento clicado.
5. Utilice `Array.prototype.map()` en los nodos recolectados para renderizar el menú y la vista de las pestañas.
6. Utilice el valor de `bindIndex` para determinar la pestaña activa y aplicar la `className` correcta.

A continuación, se muestra el código CSS para dar estilo al menú y la vista con pestañas:

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

A continuación, se muestra el código JavaScript para implementar el componente `Tabs`:

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

Finalmente, aquí está un ejemplo de cómo usar el componente `Tabs`:

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

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
