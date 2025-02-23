# Barra de desplazamiento personalizada

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para personalizar el estilo de la barra de desplazamiento para elementos con desbordamiento desplazable, puedes utilizar `::-webkit-scrollbar` para dar estilo al elemento de barra de desplazamiento, `::-webkit-scrollbar-track` para dar estilo a la pista de la barra de desplazamiento (el fondo de la barra de desplazamiento) y `::-webkit-scrollbar-thumb` para dar estilo al pulgar de la barra de desplazamiento (el elemento arrastrable). Sin embargo, ten en cuenta que esta técnica solo funciona en navegadores basados en WebKit y que el estilo de la barra de desplazamiento no está en ninguna vía estándar. Aquí hay un ejemplo de cómo utilizar estos selectores en HTML y CSS:

```html
<div class="custom-scrollbar">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.custom-scrollbar {
  height: 70px;
  overflow-y: scroll;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #1e3f20;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #4a7856;
  border-radius: 12px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
