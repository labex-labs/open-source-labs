# Padrão de Fundo de Listras (Stripes Background Pattern)

`index.html` e `style.css` já foram fornecidos na VM.

Este código cria um padrão de listras verticais em um fundo branco.

Para criar o padrão:

- Defina a propriedade `background-color` para branco.
- Use `background-image` com um valor `linear-gradient()` para criar uma listra vertical.
- Defina a propriedade `background-size` para especificar o tamanho de cada listra.
- Defina `background-repeat` para `repeat` para permitir que o padrão preencha o elemento.

Observe que a `width` e `height` fixas do elemento são apenas para fins de demonstração.

Aqui está um trecho de código de exemplo:

```html
<div class="stripes"></div>
```

```css
.stripes {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(90deg, transparent 50%, #000 50%);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
