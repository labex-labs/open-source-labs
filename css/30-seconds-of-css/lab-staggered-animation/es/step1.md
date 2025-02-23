# Animación escalonada

`index.html` y `style.css` ya se han proporcionado en la VM.

Este código crea una animación escalonada para los elementos de una lista. Para hacer esto:

1. Hacer que los elementos de la lista sean transparentes y los mueva hacia la derecha hasta el final estableciendo `opacity: 0` y `transform: translateX(100%)`.
2. Especificar las mismas propiedades `transition` para los elementos de la lista, excepto `transition-delay`.
3. Utilizar estilos en línea para especificar un valor para `--i` para cada elemento de la lista. Esto se utilizará para `transition-delay` para crear el efecto de escalonamiento.
4. Utilizar el selector pseudo-clase `:checked` para la casilla de verificación para dar estilo a los elementos de la lista. Para que aparezcan y deslicen en la vista, establezca `opacity` en `1` y `transform` en `translateX(0)`.

A continuación, se muestra el código HTML y CSS para lograr este efecto:

```html
<div class="container">
  <input type="checkbox" name="menu" id="menu" class="menu-toggler" />
  <label for="menu" class="menu-toggler-label">Menú</label>
  <ul class="stagger-menu">
    <li style="--i: 0">Inicio</li>
    <li style="--i: 1">Precios</li>
    <li style="--i: 2">Cuenta</li>
    <li style="--i: 3">Soporte</li>
    <li style="--i: 4">Acerca de</li>
  </ul>
</div>
```

```css
.container {
  overflow-x: hidden;
  width: 100%;
}

.menu-toggler {
  display: none;
}

.menu-toggler-label {
  cursor: pointer;
  font-size: 20px;
  font-weight: bold;
}

.stagger-menu {
  list-style-type: none;
  margin: 16px 0;
  padding: 0;
}

.stagger-menu li {
  margin-bottom: 8px;
  font-size: 18px;
  opacity: 0;
  transform: translateX(100%);
  transition:
    opacity 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055),
    transform 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055);
}

.menu-toggler:checked ~ .stagger-menu li {
  opacity: 1;
  transform: translateX(0);
  transition-delay: calc(0.055s * var(--i));
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
