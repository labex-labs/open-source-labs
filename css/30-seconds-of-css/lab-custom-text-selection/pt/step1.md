# Seleção de Texto Personalizada

`index.html` e `style.css` já foram fornecidos na VM.

Para modificar o estilo do texto selecionado, utilize o pseudo-seletor `::selection`. Aqui está um exemplo de trecho de código para selecionar e estilizar texto dentro de um elemento de parágrafo:

```html
<p class="custom-text-selection">Select some of this text.</p>
```

```css
::selection {
  background: aquamarine;
  color: black;
}

.custom-text-selection::selection {
  background: deeppink;
  color: white;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
