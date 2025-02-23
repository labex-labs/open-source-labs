# Texto alternante

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una animación de texto alternante, siga estos pasos:

1. Cree un elemento `<span>` con una clase de "alternating" y un `id` de "alternating-text" para contener el texto que se alternará:

```html
<p>I love coding in <span class="alternating" id="alternating-text"></span>.</p>
```

2. En el CSS, defina una animación llamada `alternating-text` que hará que el elemento `<span>` desaparezca estableciendo `display: none`:

```css
.alternating {
  animation-name: alternating-text;
  animation-duration: 3s;
  animation-iteration-count: infinite;
  animation-timing-function: ease;
}

@keyframes alternating-text {
  90% {
    display: none;
  }
}
```

3. En JavaScript, defina una matriz de las diferentes palabras que se alternarán y utilice la primera palabra para inicializar el contenido del elemento `<span>`:

```js
const texts = ["Java", "Python", "C", "C++", "C#", "Javascript"];
const element = document.getElementById("alternating-text");

let i = 0;
element.innerHTML = texts[0];
```

4. Utilice `EventTarget.addEventListener()` para definir un controlador de eventos para el evento `'animationiteration'`. Esto ejecutará el controlador de eventos cada vez que se complete una iteración de la animación. En el controlador de eventos, utilice `Element.innerHTML` para mostrar el siguiente elemento de la matriz `texts` como el contenido del elemento `<span>`:

```js
const listener = (e) => {
  i = i < texts.length - 1 ? i + 1 : 0;
  element.innerHTML = texts[i];
};

element.addEventListener("animationiteration", listener, false);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
