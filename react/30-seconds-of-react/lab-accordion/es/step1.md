# Menú desplegable tipo acordeón

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para renderizar un menú acordeón con múltiples elementos de contenido desplegables, puedes seguir estos pasos:

1. Defina un componente `AccordionItem` que renderice un `<button>` y actualice el componente mientras notifica a su padre a través de la devolución de llamada `handleClick`.
2. Utilice la propiedad `isCollapsed` en `AccordionItem` para determinar su apariencia y establecer su `className`.
3. Defina un componente `Accordion` y utilice el hook `useState()` para inicializar el valor de la variable de estado `bindIndex` con `defaultIndex`.
4. Filtrar `children` para eliminar nodos innecesarios, excepto `AccordionItem`, identificando el nombre de la función.
5. Utilice `Array.prototype.map()` en los nodos recolectados para renderizar los elementos desplegables individuales.
6. Defina `changeItem`, que se ejecutará al hacer clic en el `<button>` de un `AccordionItem`.
7. `changeItem` ejecuta la devolución de llamada pasada, `onItemClick`, y actualiza `bindIndex` según el elemento clicado.

Aquí está el código:

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

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
