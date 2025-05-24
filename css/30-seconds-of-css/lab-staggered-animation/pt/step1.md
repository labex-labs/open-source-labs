# Animação Escalonda (Staggered Animation)

`index.html` e `style.css` já foram fornecidos na VM.

Este código cria uma animação escalonada para os elementos de uma lista. Para fazer isso:

1. Torne os elementos da lista transparentes e mova-os completamente para a direita, definindo `opacity: 0` e `transform: translateX(100%)`.
2. Especifique as mesmas propriedades `transition` para os elementos da lista, exceto `transition-delay`.
3. Use estilos inline para especificar um valor para `--i` para cada elemento da lista. Isso será usado para `transition-delay` para criar o efeito escalonado.
4. Use o seletor de pseudo-classe `:checked` para a caixa de seleção (checkbox) para estilizar os elementos da lista. Para fazê-los aparecer e deslizar para a visualização, defina `opacity` para `1` e `transform` para `translateX(0)`.

Aqui está o código HTML e CSS para alcançar este efeito:

```html
<div class="container">
  <input type="checkbox" name="menu" id="menu" class="menu-toggler" />
  <label for="menu" class="menu-toggler-label">Menu</label>
  <ul class="stagger-menu">
    <li style="--i: 0">Home</li>
    <li style="--i: 1">Pricing</li>
    <li style="--i: 2">Account</li>
    <li style="--i: 3">Support</li>
    <li style="--i: 4">About</li>
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

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
