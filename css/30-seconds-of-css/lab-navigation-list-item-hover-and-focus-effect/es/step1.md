# Efecto de enfoque y de pasar el cursor en los elementos de la lista de navegación

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un efecto de enfoque y de pasar el cursor personalizado para los elementos de navegación, utiliza las transformaciones CSS de la siguiente manera:

1. Utiliza el pseudo-elemento `::before` en el ancla de la lista de elementos para crear un efecto de pasar el cursor. Ocúltilo utilizando `transform: scale(0)`.
2. Utiliza los selectores de pseudo-clases `:hover` y `:focus` para transicionar el pseudo-elemento a `transform: scale(1)` y mostrar su fondo coloreado.
3. Evita que el pseudo-elemento cubra el elemento ancla utilizando `z-index`.

Puedes utilizar el siguiente código HTML para tu menú de navegación:

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Inicio</a></li>
    <li><a href="#">Acerca de</a></li>
    <li><a href="#">Contacto</a></li>
  </ul>
</nav>
```

Y aplica las siguientes reglas CSS:

```css
.hover-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.hover-nav li {
  float: left;
}

.hover-nav li a {
  position: relative;
  display: block;
  color: #fff;
  text-align: center;
  padding: 8px 12px;
  text-decoration: none;
  z-index: 0;
}

.hover-nav li a::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: #2683f6;
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

.hover-nav li a:hover::before,
.hover-nav li a:focus::before {
  transform: scale(1);
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
