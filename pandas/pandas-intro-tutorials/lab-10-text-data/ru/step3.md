# Извлекаем фамилии из полных имен

Теперь создадим новый столбец `Surname`, который будет содержать фамилии пассажиров. Для этого мы извлечем часть имени, которая находится перед запятой в столбце `Name`.

```python
# Split the 'Name' column on comma and extract the first part
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
```
