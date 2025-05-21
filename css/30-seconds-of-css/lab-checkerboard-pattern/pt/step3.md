# Criando o Primeiro Gradiente

Agora, vamos começar a criar nosso padrão quadriculado usando gradientes CSS. Vamos adicionar o primeiro gradiente linear para criar parte do padrão.

## Compreendendo os Gradientes Lineares CSS

Os gradientes lineares CSS permitem que você crie transições suaves entre duas ou mais cores em linha reta. A função `linear-gradient()` recebe um ângulo e uma série de paradas de cor (color stops) como parâmetros. Usaremos essa técnica para criar nossos quadrados quadriculados.

Siga estes passos:

1. Abra o arquivo `style.css`.

2. Vamos modificar nossa classe `.checkerboard` para incluir o primeiro gradiente linear:

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
  );
  background-size: 60px 60px;
}
```

Deixe-me explicar o que este gradiente faz:

- `45deg` especifica o ângulo do gradiente
- `#000 25%` cria uma cor preta de 0% a 25% do espaço disponível
- `transparent 25%` cria uma cor transparente começando em 25%
- `transparent 75%` mantém a cor transparente até 75%
- `#000 75%` transiciona de volta para preto em 75% e continua até o fim
- `background-size: 60px 60px` define o tamanho de cada célula de gradiente repetida

3. Salve o arquivo `style.css`.

4. Atualize a aba **Web 8080** para ver as alterações.

Você deve agora ver um padrão começando a se formar, mas ainda não é um quadriculado completo. O primeiro gradiente cria apenas uma porção do padrão. No próximo passo, adicionaremos um segundo gradiente para completar o quadriculado.
