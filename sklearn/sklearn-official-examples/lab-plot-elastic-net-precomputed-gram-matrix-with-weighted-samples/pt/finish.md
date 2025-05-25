# Resumo

Este laboratório demonstrou como pré-calcular a matriz Gram ao usar amostras ponderadas com um modelo ElasticNet. Primeiro, carregamos um conjunto de dados de regressão e criamos um vetor de pesos log-normal, que foi normalizado para somar ao número total de amostras. Em seguida, centralizamos a matriz de projeto, redimensionamos-a pelos pesos normalizados e calculamos a matriz Gram. Finalmente, ajustamos a rede elástica usando a matriz Gram pré-calculada e os pesos normalizados.
