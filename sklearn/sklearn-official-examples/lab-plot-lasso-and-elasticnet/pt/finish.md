# Resumo

O Lasso é conhecido por recuperar dados esparsos de forma eficaz, mas não tem um bom desempenho com recursos altamente correlacionados. De fato, se vários recursos correlacionados contribuírem para o alvo, o Lasso acabaria selecionando apenas um deles. No caso de recursos esparsos, mas não correlacionados, um modelo Lasso seria mais adequado.

O ElasticNet introduz alguma esparcidade nos coeficientes e reduz seus valores a zero. Assim, na presença de recursos correlacionados que contribuem para o alvo, o modelo ainda é capaz de reduzir seus pesos sem defini-los exatamente em zero. Isso resulta em um modelo menos esparso do que um Lasso puro e pode capturar também recursos não preditivos.

O ARDRegression é melhor quando lida com ruído Gaussiano, mas ainda não consegue lidar com recursos correlacionados e requer mais tempo devido ao ajuste de uma prioridade.
