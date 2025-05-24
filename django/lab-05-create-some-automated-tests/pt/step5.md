# Ao testar, mais é melhor

Pode parecer que nossos testes estão crescendo fora de controle. Nesse ritmo, em breve haverá mais código em nossos testes do que em nossa aplicação, e a repetição é antiestética, em comparação com a concisão elegante do restante do nosso código.

**Não importa**. Deixe-os crescer. Na maior parte, você pode escrever um teste uma vez e depois esquecê-lo. Ele continuará desempenhando sua função útil à medida que você continua a desenvolver seu programa.

Às vezes, os testes precisarão ser atualizados. Suponha que alteremos nossas views para que apenas `Questions` com `Choices` sejam publicadas. Nesse caso, muitos de nossos testes existentes falharão - _dizendo-nos exatamente quais testes precisam ser alterados para atualizá-los_, de modo que, até certo ponto, os testes ajudam a cuidar de si mesmos.

Na pior das hipóteses, à medida que você continua a desenvolver, pode descobrir que tem alguns testes que agora são redundantes. Mesmo isso não é um problema; em testes, a redundância é uma coisa _boa_.

Desde que seus testes sejam organizados de forma sensata, eles não se tornarão incontroláveis. Boas regras práticas incluem ter:

- uma `TestClass` separada para cada modelo ou view
- um método de teste separado para cada conjunto de condições que você deseja testar
- nomes de métodos de teste que descrevem sua função
