# Introdução aos testes automatizados

## O que são testes automatizados?

Testes são rotinas que verificam o funcionamento do seu código.

Os testes operam em diferentes níveis. Alguns testes podem se aplicar a um detalhe minúsculo (_um determinado método do modelo retorna os valores esperados?_), enquanto outros examinam a operação geral do software (_uma sequência de entradas do usuário no site produz o resultado desejado?_). Isso não é diferente do tipo de teste que você fez anteriormente em `**Configurar o Banco de Dados**`, usando o `shell` para examinar o comportamento de um método, ou executando a aplicação e inserindo dados para verificar como ela se comporta.

O que é diferente nos testes _automatizados_ é que o trabalho de teste é feito para você pelo sistema. Você cria um conjunto de testes uma vez e, em seguida, à medida que faz alterações em seu aplicativo, pode verificar se seu código ainda funciona como você pretendia originalmente, sem ter que realizar testes manuais demorados.

## Por que você precisa criar testes

Então, por que criar testes e por que agora?

Você pode sentir que já tem bastante coisa para aprender apenas com Python/Django, e ter mais uma coisa para aprender e fazer pode parecer opressor e talvez desnecessário. Afinal, nossa aplicação de enquetes está funcionando muito bem agora; passar pelo trabalho de criar testes automatizados não vai fazê-la funcionar melhor. Se criar a aplicação de enquetes for a última coisa que você fará em programação Django, então, de fato, você não precisa saber como criar testes automatizados. Mas, se esse não for o caso, agora é um excelente momento para aprender.

### Testes economizarão seu tempo

Até certo ponto, 'verificar se parece funcionar' será um teste satisfatório. Em uma aplicação mais sofisticada, você pode ter dezenas de interações complexas entre os componentes.

Uma alteração em qualquer um desses componentes pode ter consequências inesperadas no comportamento da aplicação. Verificar se ainda 'parece funcionar' pode significar executar a funcionalidade do seu código com vinte variações diferentes dos seus dados de teste para garantir que você não quebrou nada - não é um bom uso do seu tempo.

Isso é especialmente verdade quando os testes automatizados podem fazer isso por você em segundos. Se algo deu errado, os testes também ajudarão a identificar o código que está causando o comportamento inesperado.

Às vezes, pode parecer uma tarefa árdua se afastar do seu trabalho de programação produtivo e criativo para enfrentar o negócio pouco glamouroso e pouco emocionante de escrever testes, principalmente quando você sabe que seu código está funcionando corretamente.

No entanto, a tarefa de escrever testes é muito mais gratificante do que passar horas testando sua aplicação manualmente ou tentando identificar a causa de um problema recém-introduzido.

### Testes não apenas identificam problemas, eles os previnem

É um erro pensar nos testes apenas como um aspecto negativo do desenvolvimento.

Sem testes, o propósito ou o comportamento pretendido de uma aplicação pode ser bastante opaco. Mesmo quando é seu próprio código, você às vezes se encontrará fuçando nele tentando descobrir o que exatamente ele está fazendo.

Os testes mudam isso; eles iluminam seu código por dentro e, quando algo dá errado, eles focam a luz na parte que deu errado - _mesmo que você nem tenha percebido que deu errado_.

### Testes tornam seu código mais atraente

Você pode ter criado um software brilhante, mas descobrirá que muitos outros desenvolvedores se recusarão a analisá-lo porque ele não possui testes; sem testes, eles não confiarão nele. Jacob Kaplan-Moss, um dos desenvolvedores originais do Django, diz: "Código sem testes é quebrado por design."

Que outros desenvolvedores queiram ver testes em seu software antes de levá-lo a sério é mais uma razão para você começar a escrever testes.

### Testes ajudam as equipes a trabalhar juntas

Os pontos anteriores são escritos do ponto de vista de um único desenvolvedor que mantém uma aplicação. Aplicações complexas serão mantidas por equipes. Os testes garantem que os colegas não quebrem inadvertidamente seu código (e que você não quebre o deles sem saber). Se você quer ganhar a vida como programador Django, você deve ser bom em escrever testes!
