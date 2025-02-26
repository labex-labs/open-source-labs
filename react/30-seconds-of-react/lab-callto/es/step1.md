# Enlace telefónico llamable

> `index.html` y `script.js` ya se han proporcionado en la máquina virtual. En general, solo es necesario agregar código a `script.js` y `style.css`.

Para crear un enlace que llame a un número de teléfono, use el componente `Callto`. Este componente crea un elemento `<a>` con un atributo `href` adecuado. Para renderizar el enlace, especifique el número de teléfono usando la propiedad `phone` y el texto del enlace usando la propiedad `children`.

```jsx
const Callto = ({ phone, children }) => {
  return <a href={`tel:${phone}`}>{children}</a>;
};
```

Para usar el componente `Callto`, llame al método `ReactDOM.render()` y pase el elemento `Callto` con las propiedades `phone` y `children` establecidas.

```jsx
ReactDOM.render(
  <Callto phone="+302101234567">Llámenme!</Callto>,
  document.getElementById("root")
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
