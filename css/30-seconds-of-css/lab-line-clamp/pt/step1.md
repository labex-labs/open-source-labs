# Truncar Texto Multilinha

> Você pode escrever o código em `index.html` e `style.css`.

Limitar texto multilinha a um número específico de linhas.

- Use `-webkit-line-clamp` para definir o número máximo de linhas a serem exibidas.
- Defina `display` como `-webkit-box` e `-webkit-box-orient` como `vertical`, pois são necessários para que `-webkit-line-clamp` seja aplicado.
- Aplique `overflow: hidden` para ocultar qualquer estouro (overflow) após o texto ser truncado.

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
