# Menú emergente

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para mostrar un menú emergente interactivo al pasar el cursor o al recibir el foco, siga estos pasos:

1. Utilice `left: 100%` en el CSS para posicionar el menú emergente a la derecha del elemento padre.
2. Utilice `visibility: hidden` en lugar de `display: none` para ocultar inicialmente el menú emergente y permitir que se apliquen transiciones.
3. Aplique los selectores de pseudo-clases `:hover`, `:focus` y `:focus-within` al elemento padre para mostrar el menú emergente cuando se pase el cursor o se reciba el foco.
4. Utilice el siguiente código HTML y CSS:

HTML:

```
<div class="reference" tabindex="0">
  <div class="popout-menu">Menú emergente</div>
</div>
```

CSS:

```
.reference {
  position: relative;
  background: tomato;
  width: 100px;
  height: 80px;
}

.popout-menu {
  position: absolute;
  visibility: hidden;
  left: 100%;
  background: #9C27B0;
  color: white;
  padding: 16px;
}

.reference:hover >.popout-menu,
.reference:focus >.popout-menu,
.reference:focus-within >.popout-menu {
  visibility: visible;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
