# Contenido collapsible

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Esta función renderiza un componente collapsible con un botón que alterna la visibilidad de su contenido. Aquí está cómo se utiliza:

1. Utilice el hook `useState()` para crear la variable de estado `isCollapsed`, que representa si el contenido está actualmente contraído o expandido. Inicialícela en `collapsed`.
2. Utilice el elemento `<button>` para alternar el estado `isCollapsed` y mostrar/ocultar el contenido pasado a través de la propiedad `children`.
3. Utilice `isCollapsed` para aplicar la clase CSS adecuada al contenedor de contenido, ya sea `collapsed` o `expanded`, lo que determina su apariencia.
4. Actualice el atributo `aria-expanded` del contenedor de contenido según el estado `isCollapsed`, para que el componente sea accesible para usuarios con discapacidades.

Aquí está el código CSS necesario para este componente:

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

Y aquí está el código JavaScript:

```jsx
const Collapse = ({ collapsed, children }) => {
  const [isCollapsed, setIsCollapsed] = React.useState(collapsed);

  return (
    <>
      <button
        className="collapse-button"
        onClick={() => setIsCollapsed(!isCollapsed)}
      >
        {isCollapsed ? "Mostrar" : "Ocultar"} contenido
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

Para utilizar este componente, simplemente llámelo con el contenido que desea contraer:

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Collapse>
    <h1>Esto es un collapse</h1>
    <p>Hola mundo!</p>
  </Collapse>
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
