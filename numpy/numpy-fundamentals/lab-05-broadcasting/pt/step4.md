# Regras Gerais de Broadcasting

NumPy compara os formatos de dois arrays elemento a elemento para determinar se eles são compatíveis para broadcasting (difusão). As seguintes regras se aplicam:

1. Duas dimensões são compatíveis se tiverem o mesmo tamanho.
2. Duas dimensões são compatíveis se uma delas tiver tamanho 1.

Se essas condições não forem atendidas, um `ValueError` é levantado, indicando que os arrays têm formatos incompatíveis.
