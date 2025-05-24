# Centralização em Grade (Grid Centering)

`index.html` e `style.css` já foram fornecidos na VM.

Para centralizar um elemento filho tanto horizontalmente quanto verticalmente dentro de um elemento pai, siga estes passos:

1.  Crie um layout de grade (grid layout) usando `display: grid`.
2.  Use `justify-content: center` para centralizar o filho horizontalmente.
3.  Use `align-items: center` para centralizar o filho verticalmente.

Aqui está um exemplo de estrutura HTML:

```html
<div class="parent">
  <div class="child">Conteúdo centralizado.</div>
</div>
```

E o CSS correspondente:

```css
.parent {
  display: grid;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
