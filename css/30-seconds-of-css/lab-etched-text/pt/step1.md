# Texto Gravado (Etched Text)

`index.html` e `style.css` já foram fornecidos na VM.

Para criar um efeito "gravado" ou entalhado para texto em um fundo, use as seguintes propriedades CSS:

```css
.etched-text {
  text-shadow: 0 2px white;
  font-size: 1.5rem;
  font-weight: bold;
  color: #b8bec5;
}
```

A propriedade `text-shadow` cria uma sombra branca deslocada em `0px` horizontalmente e `2px` verticalmente da posição de origem. Certifique-se de que o fundo seja mais escuro que a sombra para que o efeito funcione. Adicionalmente, a cor do texto deve ser ligeiramente desbotada para que pareça ter sido esculpida no fundo. Finalmente, aplique a classe `etched-text` ao elemento HTML desejado, como um parágrafo, para obter o efeito.

```html
<p class="etched-text">Eu pareço gravado no fundo.</p>
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
