# Statistiken aggregieren, gruppiert nach Kategorie

Als nächstes werden wir lernen, wie man Statistiken aggregiert, die nach Kategorie gruppiert sind.

```python
# Computing the average age for male versus female Titanic passengers
average_age_sex = titanic[["Sex", "Age"]].groupby("Sex").mean()
# Printing the result
print(f"The average age for male versus female Titanic passengers is {average_age_sex}")

# Computing the mean ticket fare price for each of the sex and cabin class combinations
mean_fare_sex_class = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
# Printing the result
print(f"The mean ticket fare price for each of the sex and cabin class combinations is {mean_fare_sex_class}")
```
