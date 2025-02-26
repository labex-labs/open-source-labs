# Hook useIntersectionObserver de React

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para observar los cambios de visibilidad de un elemento dado, siga estos pasos:

1. Utilice el hook `useState()` para almacenar el valor de intersección del elemento dado.
2. Cree un `IntersectionObserver` con las `opciones` dadas y una devolución de llamada adecuada para actualizar la variable de estado `isIntersecting`.
3. Utilice el hook `useEffect()` para llamar a `IntersectionObserver.observe()` al montar el componente y limpiar usando `IntersectionObserver.unobserve()` al desmontar.

A continuación, se muestra una implementación de ejemplo:

```jsx
const useIntersectionObserver = (ref, options) => {
  const [isIntersecting, setIsIntersecting] = React.useState(false);

  React.useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      setIsIntersecting(entry.isIntersecting);
    }, options);

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      observer.unobserve(ref.current);
    };
  }, [ref, options]);

  return isIntersecting;
};
```

Puede usar el hook `useIntersectionObserver` de la siguiente manera:

```jsx
const MyApp = () => {
  const ref = React.useRef();
  const onScreen = useIntersectionObserver(ref, { threshold: 0.5 });

  return (
    <div>
      <div style={{ height: "100vh" }}>Desplácese hacia abajo</div>
      <div style={{ height: "100vh" }} ref={ref}>
        <p>
          {onScreen ? "El elemento está en la pantalla." : "Desplácese más!"}
        </p>
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
