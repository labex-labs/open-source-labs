# Desplazamiento horizontal con "snap"

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un contenedor horizontalmente desplazable que se ajuste a los elementos al hacer scroll, siga estos pasos:

1. Utilice `display: grid` y `grid-auto-flow: column` para crear un diseño horizontal.
2. Utilice `scroll-snap-type: x mandatory` y `overscroll-behavior-x: contain` para crear un efecto de ajuste en el desplazamiento horizontal.
3. Cambie `scroll-snap-align` a `start`, `stop` o `center` para ajustar el alineamiento del ajuste.

A continuación, se muestra un ejemplo de código HTML y CSS que puede utilizar:

HTML

```
<div class="horizontal-snap">
  <a href="#"><img src="https://picsum.photos/id/1067/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/122/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/188/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/249/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/257/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/259/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/283/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/288/640/640"></a>
  <a href="#"><img src="https://picsum.photos/id/299/640/640"></a>
</div>
```

CSS

```
.horizontal-snap {
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  height: calc(180px + 1rem);
  padding: 1rem;
  max-width: 480px;
  margin: 0 auto;
  overflow-y: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
}

.horizontal-snap > a {
  scroll-snap-align: center;
}

.horizontal-snap img {
  width: 180px;
  max-width: none;
  object-fit: contain;
  border-radius: 1rem;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
