# Sibling Fade (Desvanecimento de Irmãos)

`index.html` e `style.css` já foram fornecidos na VM (Máquina Virtual).

Para desvanecer os irmãos de um item em foco:

1. Anime as mudanças na `opacity` (opacidade) usando a propriedade `transition` (transição).

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}
```

2. Mude a `opacity` de todos os elementos, exceto o que o mouse está sobre, para `0.5` usando os seletores de pseudo-classe `:hover` e `:not`.

```css
.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```

Aqui está um exemplo de código HTML:

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

Por favor, clique em 'Go Live' (Iniciar) no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
