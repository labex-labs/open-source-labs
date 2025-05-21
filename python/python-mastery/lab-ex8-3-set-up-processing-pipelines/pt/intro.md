# Introdução

Neste laboratório, você aprenderá como usar corrotinas para construir pipelines de processamento de dados. Corrotinas, um recurso poderoso do Python, suportam multitarefa cooperativa, permitindo que funções pausem e retomem a execução em um ponto posterior.

Os objetivos deste laboratório são entender como as corrotinas funcionam em Python, implementar pipelines de processamento de dados baseados em corrotinas e transformar dados através de múltiplos estágios de corrotinas. Você criará dois arquivos: `cofollow.py`, um seguidor de arquivo baseado em corrotinas, e `coticker.py`, uma aplicação de ticker de ações usando corrotinas. Assume-se que o programa `stocksim.py` de um exercício anterior ainda está sendo executado em segundo plano, gerando dados de ações em um arquivo de log.
