# Exercício 8.3: Adicionando `Logging` a um Programa

Para adicionar `logging` a uma aplicação, você precisa ter algum mecanismo para inicializar o módulo `logging` no módulo principal. Uma maneira de fazer isso é incluir algum código de configuração que se parece com isto:

    # Este arquivo configura a configuração básica do módulo logging.
    # Altere as configurações aqui para ajustar a saída de logging conforme necessário.
    import logging
    logging.basicConfig(
        filename = 'app.log',            # Nome do arquivo de log (omita para usar stderr)
        filemode = 'w',                  # Modo do arquivo (use 'a' para anexar)
        level    = logging.WARNING,      # Nível de logging (DEBUG, INFO, WARNING, ERROR, ou CRITICAL)
    )

Novamente, você precisaria colocar isso em algum lugar nos passos de inicialização do seu programa. Por exemplo, onde você colocaria isso no seu programa `report.py`?
