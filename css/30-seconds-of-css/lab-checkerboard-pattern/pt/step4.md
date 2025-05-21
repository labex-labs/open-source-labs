# Completando o Padrão Quadriculado

Agora, vamos adicionar o segundo gradiente linear para completar nosso padrão quadriculado e torná-lo repetível em todo o elemento.

1. Abra o arquivo `style.css` novamente.

2. Modifique a classe `.checkerboard` para incluir um segundo gradiente linear que criará o padrão alternado:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ), linear-gradient(-45deg, #000 25%, transparent 25%, transparent 75%, #000
        75%, #000);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

O que adicionamos:

- Um segundo `linear-gradient()` que é semelhante ao primeiro, mas com um ângulo de `-45deg` para criar o padrão alternado
- A propriedade `background-repeat: repeat` garante que os padrões se repitam em todo o elemento

A combinação desses dois gradientes em ângulos diferentes cria o clássico padrão quadriculado. O primeiro gradiente cria um conjunto de quadrados diagonais, enquanto o segundo gradiente cria outro conjunto que preenche as lacunas.

3. Salve o arquivo `style.css`.

4. Atualize a aba **Web 8080** para ver o resultado final.

Você deve agora ver um padrão quadriculado completo com quadrados pretos e brancos alternados. O padrão deve se repetir em todo o elemento de 240px por 240px.

## Como o Padrão Funciona

O efeito quadriculado é criado por:

1. Usando dois gradientes lineares com ângulos opostos (45deg e -45deg)
2. Cada gradiente cria um padrão de quadrados pretos nos cantos
3. As áreas transparentes permitem que o fundo branco apareça
4. A propriedade `background-size` controla o tamanho de cada quadrado no padrão
5. A propriedade `background-repeat` faz com que o padrão se repita em todo o elemento

Esta técnica demonstra o poder dos gradientes CSS para criar padrões complexos sem a necessidade de arquivos de imagem, resultando em tempos de carregamento mais rápidos e melhor escalabilidade.
