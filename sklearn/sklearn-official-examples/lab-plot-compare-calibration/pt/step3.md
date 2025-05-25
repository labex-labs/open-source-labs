# Interpretar Curvas de Calibração

As curvas de calibração mostram a relação entre as probabilidades previstas e os resultados reais para cada modelo. Modelos bem calibrados produzem curvas que seguem a linha diagonal, indicando que as probabilidades previstas correspondem aos resultados reais. Os quatro modelos produzem resultados diferentes:

- A regressão logística produz previsões bem calibradas, pois otimiza diretamente a perda de log.
- O Naive Bayes Gaussiano tende a empurrar as probabilidades para 0 ou 1, principalmente porque a equação do Naive Bayes apenas fornece uma estimativa correta das probabilidades quando a suposição de que as características são condicionalmente independentes se mantém.
- O Classificador de Floresta Aleatória apresenta o comportamento oposto: os histogramas mostram picos em aproximadamente 0,2 e 0,9 de probabilidade, enquanto as probabilidades próximas de 0 ou 1 são muito raras.
- O SVM linear mostra uma curva ainda mais sigmoide do que o Classificador de Floresta Aleatória, o que é típico dos métodos de margem máxima.
