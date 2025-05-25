# Estrutura da Aplicação

A organização do código e a estrutura de arquivos são fundamentais para a manutenibilidade de uma aplicação.

Não existe uma abordagem "tamanho único" para Python. No entanto, uma estrutura que funciona para muitos problemas é algo como isto.

```code
porty-app/
  README.txt
  script.py         # SCRIPT
  porty/
    # CÓDIGO DA BIBLIOTECA
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

O nível superior `porty-app` é um contêiner para todo o resto -- documentação, scripts de nível superior, exemplos, etc.

Novamente, os scripts de nível superior (se houver) precisam existir fora do pacote de código. Um nível acima.

```python
#!/usr/bin/env python3
# porty-app/script.py
import sys
import porty

porty.report.main(sys.argv)
```

Neste ponto, você tem um diretório com vários programas:

    pcost.py          # calcula o custo do portfólio
    report.py         # Cria um relatório
    ticker.py         # Produz um ticker de ações em tempo real

Há uma variedade de módulos de suporte com outras funcionalidades:

    stock.py          # Classe Stock
    portfolio.py      # Classe Portfolio
    fileparse.py      # Parsing CSV
    tableformat.py    # Tabelas formatadas
    follow.py         # Seguir um arquivo de log
    typedproperty.py  # Propriedades de classe tipadas

Neste exercício, vamos limpar o código e colocá-lo em um pacote comum.
