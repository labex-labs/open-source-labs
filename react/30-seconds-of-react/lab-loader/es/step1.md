# Cargador Giratorio

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

**Renderiza un componente de cargador giratorio.**

Para renderizar un componente de cargador giratorio, siga estos pasos:

1. Renderice un elemento SVG cuyas dimensiones están determinadas por la propiedad `size`.
2. Utilice CSS para animar el SVG, creando una animación de giro. Específicamente, agregue la clase `.loader` al SVG y establezca la propiedad `animation` en `rotate 2s linear infinite`. Además, defina las claves de animación `rotate` con una propiedad `transform` que rote el SVG 360 grados.
3. Agregue un elemento `circle` al SVG, que representa el círculo giratorio. Para animar el círculo, agregue el selector `.loader circle` y establezca la propiedad `animation` en `dash 1.5s ease-in-out infinite`. Además, defina las claves de animación `dash` con las propiedades `stroke-dasharray` y `stroke-dashoffset` que crean un patrón de trazo discontinuo que se mueve alrededor del círculo.
4. Finalmente, cree un componente `Loader` que renderice el SVG con la propiedad `size` pasada como atributos de ancho y alto.

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

Para usar el componente `Loader` con un tamaño de 24, llame a `ReactDOM.createRoot(document.getElementById('root')).render(<Loader size={24} />);`.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
