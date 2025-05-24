# Círculo

`index.html` e `style.css` já foram fornecidos na VM.

Para criar uma forma circular usando CSS puro, use a propriedade `border-radius: 50%` para curvar as bordas do elemento. Certifique-se de definir tanto `width` quanto `height` para o mesmo valor para garantir um círculo perfeito. Se valores diferentes forem usados, uma elipse será criada em vez disso. Aqui está um trecho de código de exemplo:

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
