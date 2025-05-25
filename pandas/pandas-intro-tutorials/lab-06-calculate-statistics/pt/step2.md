# Calculando Estatísticas Sumárias

Nesta etapa, calcularemos as estatísticas sumárias para o conjunto de dados do Titanic.

```python
# Computing the average age of the Titanic passengers
average_age = titanic["Age"].mean()
# Printing the result
print(f"The average age of the Titanic passengers is {average_age}")

# Computing the median age and ticket fare price of the Titanic passengers
median_age_fare = titanic[["Age", "Fare"]].median()
# Printing the result
print(f"The median age and ticket fare price of the Titanic passengers are {median_age_fare}")
```
