# Melhores Práticas para Exceções (Exception Best Practices)

Não capture exceções. Falhe rápido e alto. Se for importante, outra pessoa cuidará do problema. Capture uma exceção apenas se você for _essa_ pessoa. Ou seja, capture apenas erros onde você pode se recuperar e continuar de forma sensata.
