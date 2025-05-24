# Truncar Texto

`index.html` e `style.css` já foram fornecidos na VM.

Para truncar texto que é maior que uma linha e adicionar uma elipse no final, use as seguintes propriedades CSS:

- `overflow: hidden` para evitar que o texto transborde suas dimensões
- `white-space: nowrap` para evitar que o texto exceda uma linha em altura
- `text-overflow: ellipsis` para adicionar uma elipse se o texto exceder suas dimensões
- Especifique uma `width` (largura) fixa para o elemento para saber quando exibir uma elipse

Observe que este método só funciona para elementos de uma única linha. Por exemplo:

```html
<p class="truncate-text">If I exceed one line's width, I will be truncated.</p>
```

```css
.truncate-text {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 200px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
