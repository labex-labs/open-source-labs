# Definir Dados

Em seguida, precisamos definir os dados que serão plotados. Neste exemplo, temos um conjunto de observações com quatro variáveis: nome, movimento próprio angular (angular proper motion), erro do movimento próprio angular (angular proper motion error) e distância. Converteremos o movimento próprio angular em velocidade linear e o plotaremos em relação ao FWHM (full width at half maximum) das observações.

```python
obs = [["01_S1", 3.88, 0.14, 1970, 63],
       ["01_S4", 5.6, 0.82, 1622, 150],
       ["02_S1", 2.4, 0.54, 1570, 40],
       ["03_S1", 4.1, 0.62, 2380, 170]]

# Fator de conversão do movimento próprio angular para velocidade linear
pm_to_kms = 1./206265.*2300*3.085e18/3.15e7/1.e5
```
