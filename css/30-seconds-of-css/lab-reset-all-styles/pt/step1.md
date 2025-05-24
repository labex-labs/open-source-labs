# Redefinir Todos os Estilos

`index.html` e `style.css` já foram fornecidos na VM (Virtual Machine).

Para redefinir todos os estilos para seus valores padrão, use a propriedade `all`. Esta propriedade não afetará as propriedades `direction` e `unicode-bidi`. Aqui está um exemplo de como usá-la:

```html
<div class="reset-all-styles">
  <h5>Title</h5>
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure id
    exercitationem nulla qui repellat laborum vitae, molestias tempora velit
    natus. Quas, assumenda nisi. Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.reset-all-styles {
  all: initial;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
