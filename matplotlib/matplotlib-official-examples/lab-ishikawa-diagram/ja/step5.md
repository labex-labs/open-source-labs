# 入力データ

ここでは、入力データを定義します。データは辞書で、キーがカテゴリで、値が原因のリストである必要があります。

```python
categories = {
    'Method': ['Time consumption', 'Cost', 'Procedures', 'Inefficient process', 'Sampling'],
    'Machine': ['Faulty equipment', 'Compatibility'],
    'Material': ['Poor-quality input', 'Raw materials', 'Supplier', 'Shortage'],
    'Measurement': ['Calibration', 'Performance', 'Wrong measurements'],
    'Environment': ['Bad conditions'],
    'People': ['Lack of training', 'Managers', 'Labor shortage', 'Procedures', 'Sales strategy']
}
```
