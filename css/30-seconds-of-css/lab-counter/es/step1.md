# Contador

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un contador de lista personalizado que cuente los elementos de lista anidados, siga estos pasos:

1. Utilice `counter-reset` para inicializar una variable de contador (valor predeterminado `0`), con el nombre siendo el valor del atributo (por ejemplo, `counter`).
2. Utilice `counter-increment` en la variable de contador para cada elemento contable (por ejemplo, cada `<li>`).
3. Utilice `counters()` para mostrar el valor de cada variable de contador como parte del `content` del pseudo-elemento `::before` para cada elemento contable (por ejemplo, cada `<li>`). El segundo valor que se le pasa (`'.'`) actúa como el delimitador para los contadores anidados.

A continuación, se muestra un ejemplo de código HTML:

```html
<ul>
  <li>Elemento de lista</li>
  <li>Elemento de lista</li>
  <li>
    Elemento de lista
    <ul>
      <li>Elemento de lista</li>
      <li>Elemento de lista</li>
      <li>Elemento de lista</li>
    </ul>
  </li>
</ul>
```

Y aquí está el código CSS para aplicar el contador de lista personalizado:

```css
ul {
  counter-reset: counter;
  list-style: none;
}

li::before {
  counter-increment: counter;
  content: counters(counter, ".") " ";
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
