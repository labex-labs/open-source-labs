# Resumo

Neste laboratório, aprendemos a utilizar o scikit-learn para classificação de texto usando aprendizado fora da memória. Usamos um classificador online que suporta o método `partial_fit`, alimentado com lotes de exemplos. Também aproveitamos um `HashingVectorizer` para garantir que o espaço de características permanecesse o mesmo ao longo do tempo. Em seguida, reservamos um conjunto de teste e iteramos sobre mini-lotes de exemplos para atualizar os classificadores. Finalmente, plotamos os resultados para visualizar a evolução da precisão e os tempos de treinamento.
