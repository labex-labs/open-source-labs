# Erstellen einer praktischen Anwendung: Abonnementrechner

Nachdem wir nun eine zuverlässige Funktion zur Berechnung von Monatsdifferenzen haben, wenden wir sie auf ein reales Szenario an. Wir werden einen Abonnementrechner erstellen, der die Kosten eines Service-Abonnements zwischen zwei Daten berechnet.

Erstellen Sie eine neue Datei namens `subscription_calculator.py` im Verzeichnis `/home/labex/project`:

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

Speichern Sie die Datei und führen Sie sie aus:

```bash
python3 ~/project/subscription_calculator.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen (die Testzeitraum-Daten zeigen Ihr aktuelles Datum):

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

Diese Anwendung zeigt, wie unsere `months_diff`-Funktion in einem praktischen Szenario eingesetzt werden kann:

1. Wir berechnen die Gesamtkosten eines Abonnements basierend auf der Anzahl der Monate zwischen zwei Daten.
2. Wir vergleichen diese Kosten mit einem Jahresplan, um einem Benutzer zu helfen, zu entscheiden, welcher Plan wirtschaftlicher ist.
3. Wir berechnen die Kosten für einen kurzen Testzeitraum.

Beachten Sie, dass auch der 7-Tage-Testzeitraum in unserem Modell als ein ganzer Monat berechnet wird. Dies liegt daran, dass unsere Funktion jeden Teilmonat auf einen vollen Monat aufrundet, was bei der Abrechnung von Abonnements üblich ist.

Diese Art der Berechnung wird häufig in folgenden Bereichen verwendet:

- Abonnementdiensten (Streaming, Software, Mitgliedschaften)
- Kredit- und Hypothekenberechnungen
- Mietverträgen
- Projektabrechnungen
