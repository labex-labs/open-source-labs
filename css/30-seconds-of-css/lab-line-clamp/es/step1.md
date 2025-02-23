# Recortar texto multilínea

> Puedes escribir el código en `index.html` y `style.css`..

Limita el texto multilínea a un número determinado de líneas.

- Utiliza `-webkit-line-clamp` para establecer el número máximo de líneas que se mostrarán.
- Establece `display` en `-webkit-box` y `-webkit-box-orient` en `vertical`, ya que son necesarios para que se aplique `-webkit-line-clamp`.
- Aplica `overflow: hidden` para ocultar cualquier desbordamiento después de que se recorte el texto.

```html
<p class="excerpt">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod enim
  eget ultricies sollicitudin. Nunc aliquam arcu arcu, non suscipit metus luctus
  id. Aliquam sodales turpis ipsum, in vehicula dui tempor sit amet. Nullam quis
  urna erat. Pellentesque mattis dolor purus. Aliquam nisl urna, tempor a
  euismod a, placerat in mauris. Phasellus neque quam, dapibus quis nunc at,
  feugiat suscipit tortor. Duis vel posuere dolor. Phasellus risus erat,
  lobortis et mi vel, viverra faucibus lectus. Etiam ut posuere sapien. Nulla
  ultrices dui turpis, interdum consectetur urna tempus at.
</p>
```

```css
.excerpt {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```
