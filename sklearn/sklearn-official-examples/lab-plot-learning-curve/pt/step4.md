# Analisar as curvas de aprendizagem

```python
# Interpretar as curvas de aprendizagem
```

Podemos analisar a curva de aprendizagem do classificador Naive Bayes. Sua forma pode ser encontrada frequentemente em conjuntos de dados mais complexos: a pontuação de treinamento é muito alta ao usar poucas amostras para treinamento e diminui ao aumentar o número de amostras, enquanto a pontuação de teste é muito baixa no início e depois aumenta ao adicionar amostras. As pontuações de treinamento e teste tornam-se mais realistas quando todas as amostras são usadas para treinamento.

Observamos outra curva de aprendizagem típica para o classificador SVM com kernel RBF. A pontuação de treinamento permanece alta, independentemente do tamanho do conjunto de treinamento. Por outro lado, a pontuação de teste aumenta com o tamanho do conjunto de dados de treinamento. De fato, ela aumenta até um ponto em que atinge um platô. Observar tal platô é uma indicação de que pode não ser útil adquirir novos dados para treinar o modelo, pois o desempenho de generalização do modelo não aumentará mais.
