# Compreendendo a Estrutura HTML

Antes de começarmos a criar nossa animação, precisamos entender a estrutura HTML com a qual trabalharemos. Nesta etapa, examinaremos o arquivo HTML fornecido e faremos as modificações necessárias.

1. Abra o arquivo `index.html` no editor.

2. Se o arquivo estiver vazio ou ausente, crie-o com o seguinte conteúdo:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zoom In Zoom Out Animation</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>CSS Animation Demo</h1>
    <p>This box demonstrates a zoom in zoom out animation:</p>

    <div class="zoom-in-out-box"></div>
  </body>
</html>
```

3. Vamos entender o que este HTML faz:

   - Temos uma estrutura de documento HTML padrão com um título e configurações de viewport (área de visualização)
   - Vinculamos a um arquivo CSS externo chamado `style.css`
   - Incluímos um cabeçalho e um parágrafo para explicar nossa demonstração
   - Mais importante, temos um elemento `<div>` com a classe `zoom-in-out-box` que será animado

4. Salve o arquivo `index.html` se você fez alguma alteração.

Este elemento div será nossa tela para criar a animação. Na próxima etapa, estilaremos este elemento usando CSS.
