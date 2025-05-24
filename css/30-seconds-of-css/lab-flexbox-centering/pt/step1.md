# Centralização com Flexbox

`index.html` e `style.css` já foram fornecidos na VM.

Para centralizar um elemento filho tanto horizontalmente quanto verticalmente dentro de um elemento pai usando flexbox, siga estes passos:

1.  Crie um layout flexbox definindo a propriedade `display` do elemento pai como `flex`.
2.  Use a propriedade `justify-content` para centralizar o filho horizontalmente, definindo seu valor como `center`.
3.  Use a propriedade `align-items` para centralizar o filho verticalmente, definindo seu valor como `center`.
4.  Adicione o elemento filho dentro do elemento pai.

Aqui está um trecho de código de exemplo:

```html
<div class="flexbox-centering">
  <div>Conteúdo centralizado.</div>
</div>
```

```css
.flexbox-centering {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
