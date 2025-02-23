# Efecto de enlace de onda al pasar el cursor

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un efecto de onda al pasar el cursor sobre un enlace, puedes seguir estos pasos:

1. Crea un fondo repetitivo para el enlace usando un `linear-gradient`.

```css
a.squiggle {
  background: linear-gradient(to bottom, #0087ca 0%, #0087ca 100%);
  background-position: 0 100%;
  background-repeat: repeat-x;
  background-size: 2px 2px;
  color: inherit;
  text-decoration: none;
}
```

2. Crea un estado `:hover` para el enlace con una `background-image` de una URL de datos que contiene un SVG con una ruta ondulante y una animación.

```css
a.squiggle:hover {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 4'%3E%3Cstyle type='text/css'%3E.squiggle{animation:shift.3s linear infinite;}@keyframes shift {from {transform:translateX(0);}to {transform:translateX(-15px);}}%3C/style%3E%3Cpath fill='none' stroke='%230087ca' stroke-width='2' class='squiggle' d='M0,3.5 c 5,0,5,-3,10,-3 s 5,3,10,3 c 5,0,5,-3,10,-3 s 5,3,10,3'/%3E%3C/svg%3E");
  background-size: auto 4px;
}
```

3. Utiliza el código HTML siguiente para agregar el enlace a la página.

```html
<p>El <a class="squiggle" href="#">imponente pulpo</a> nadó con gracia.</p>
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
