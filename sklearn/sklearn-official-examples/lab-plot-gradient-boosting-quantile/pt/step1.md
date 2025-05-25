# Gerar Dados Sintéticos

Vamos gerar dados sintéticos para um problema de regressão aplicando a função a entradas aleatórias amostradas uniformemente. Para tornar o problema mais interessante, geramos observações do alvo y como a soma de um termo determinístico calculado pela função f e um termo de ruído aleatório que segue uma distribuição log-normal centrada. A distribuição log-normal é assimétrica e tem caudas longas: observar outliers grandes é provável, mas é impossível observar outliers pequenos.
