# Distribuição Uniforme de Filhos (Evenly Distributed Children)

`index.html` e `style.css` já foram fornecidos na VM.

Para distribuir uniformemente os elementos filhos dentro de um elemento pai, use o layout flexbox, definindo a propriedade `display` do elemento pai como `flex`. Para distribuir os filhos horizontalmente com espaço igual entre eles, use `justify-content: space-between`. Para distribuir os filhos com espaço ao redor deles, use `justify-content: space-around`. Aqui está um exemplo:

```html
<div class="evenly-distributed-children">
  <p>Item1</p>
  <p>Item2</p>
  <p>Item3</p>
</div>
```

```css
.evenly-distributed-children {
  display: flex;
  justify-content: space-between;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
