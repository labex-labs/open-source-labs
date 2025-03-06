# Création d'une application pratique : Calculateur d'abonnement

Maintenant que nous avons une fonction fiable pour calculer les différences de mois, appliquons-la à un scénario du monde réel. Nous allons créer un calculateur d'abonnement qui détermine le coût d'un abonnement à un service entre deux dates.

Créez un nouveau fichier appelé `subscription_calculator.py` dans le répertoire `/home/labex/project` :

```python
from datetime import date, timedelta
from month_difference import months_diff

def calculate_subscription_cost(start_date, end_date, monthly_fee):
    """
    Calculate the total cost of a subscription between two dates.

    Args:
        start_date (date): Subscription start date
        end_date (date): Subscription end date
        monthly_fee (float): Cost per month

    Returns:
        float: Total subscription cost
    """
    # Calculate number of months
    months = months_diff(start_date, end_date)

    # Calculate total cost
    total_cost = months * monthly_fee

    return total_cost

# Example: Calculate subscription cost for a streaming service
start = date(2023, 1, 15)  # Subscription starts January 15, 2023
end = date(2023, 8, 20)    # Ends August 20, 2023
monthly_cost = 9.99        # $9.99 per month

total = calculate_subscription_cost(start, end, monthly_cost)
print(f"Subscription period: {start} to {end}")
print(f"Monthly fee: ${monthly_cost:.2f}")
print(f"Total cost: ${total:.2f}")

# Compare with an annual plan
annual_cost = 99.99  # $99.99 per year
print(f"\nAnnual plan cost: ${annual_cost:.2f}")
print(f"Monthly plan for same period: ${total:.2f}")

if total > annual_cost:
    print(f"Savings with annual plan: ${total - annual_cost:.2f}")
else:
    print(f"Additional cost for annual plan: ${annual_cost - total:.2f}")

# Calculate cost for a trial period
today = date.today()
trial_end = today + timedelta(days=7)  # 7-day trial
trial_cost = calculate_subscription_cost(today, trial_end, monthly_cost)
print(f"\nOne-week trial period: {today} to {trial_end}")
print(f"Trial period cost: ${trial_cost:.2f}")
```

Enregistrez le fichier et exécutez-le :

```bash
python3 ~/project/subscription_calculator.py
```

Vous devriez voir une sortie similaire à celle-ci (les dates d'essai afficheront votre date actuelle) :

```
Subscription period: 2023-01-15 to 2023-08-20
Monthly fee: $9.99
Total cost: $79.92

Annual plan cost: $99.99
Monthly plan for same period: $79.92
Additional cost for annual plan: $20.07

One-week trial period: 2023-06-01 to 2023-06-08
Trial period cost: $9.99
```

Cette application montre comment notre fonction `months_diff` peut être utilisée dans un scénario pratique :

1. Nous calculons le coût total d'un abonnement en fonction du nombre de mois entre deux dates
2. Nous comparons ce coût avec un forfait annuel pour aider un utilisateur à décider quel forfait est le plus économique
3. Nous calculons le coût d'une courte période d'essai

Remarquez comment même la période d'essai de 7 jours est facturée comme un mois entier dans notre modèle. C'est parce que notre fonction arrondit tout mois partiel à un mois entier, ce qui est courant dans la facturation des abonnements.

Ce type de calcul est fréquemment utilisé dans :

- Les services d'abonnement (streaming, logiciels, adhésions)
- Les calculs de prêts et de hypothèques
- Les contrats de location
- La facturation de projets
