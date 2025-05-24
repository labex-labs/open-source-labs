# Resumo

Neste laboratório, você criou seus primeiros contêineres Ubuntu, Nginx e MongoDB.

Principais Conclusões

- Os contêineres são compostos por namespaces Linux e grupos de controle que fornecem isolamento de outros contêineres e do host.
- Devido às propriedades de isolamento dos contêineres, você pode agendar muitos contêineres em um único host sem se preocupar com dependências conflitantes. Isso facilita a execução de vários contêineres em um único host: utilizando totalmente os recursos alocados para esse host e, em última análise, economizando algum dinheiro com os custos do servidor.
- Evite usar conteúdo não verificado da Docker Store ao desenvolver suas próprias imagens, pois essas imagens podem conter vulnerabilidades de segurança ou possivelmente até mesmo software malicioso.
- Os contêineres incluem tudo o que precisam para executar os processos dentro deles, portanto, não há necessidade de instalar dependências adicionais diretamente em seu host.
