# Загружаем данные

В этом уроке мы будем использовать данные о качестве воздуха. Данные будут загружены из CSV-файла в DataFrame Pandas.

```python
# Loading the data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```
