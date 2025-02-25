# Exercice 1.7 : Hypothèque de Dave

Dave a décidé de souscrire une hypothèque à taux fixe de 30 ans de 500 000 \$ auprès de la société de crédit immobilier, d'investissement en actions et de trading de Bitcoin de Guido. Le taux d'intérêt est de 5 % et le paiement mensuel est de 2684,11 \$.

Voici un programme qui calcule le montant total que Dave devra payer au cours de la durée de l'hypothèque :

```python
# mortgage.py

principal = 500000.0
taux = 0.05
paiement = 2684.11
total_payé = 0.0

while principal > 0:
    principal = principal * (1+taux/12) - paiement
    total_payé = total_payé + paiement

print('Total payé', total_payé)
```

Entrez ce programme et exécutez-le. Vous devriez obtenir une réponse de `966279.5999999957`.
