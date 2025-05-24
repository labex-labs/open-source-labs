# Tipografia Fluida

`index.html` e `style.css` já foram fornecidos na VM (Máquina Virtual).

Para criar texto que se ajusta em tamanho com base na largura da viewport, você pode usar CSS. Uma maneira de fazer isso é usando a função `clamp()` para definir os tamanhos de fonte mínimo e máximo. Outra maneira é usar uma fórmula para calcular um valor responsivo para o tamanho da fonte. Aqui está um exemplo de elemento HTML com a classe `fluid-type`:

```html
<p class="fluid-type">Hello World!</p>
```

Aqui está o código CSS correspondente que define o tamanho da fonte para ajustar entre `1rem` e `3rem` com base na largura da viewport:

```css
.fluid-type {
  font-size: clamp(1rem, 8vw - 2rem, 3rem);
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
