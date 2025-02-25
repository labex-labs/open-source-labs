# データを準備する

SkewT - logP図用のデータを準備します。文字列を読み取るためにStringIOモジュールと、配列に読み込むためにNumPyを使用します。

```python
data_txt = '''
        978.0    345    7.8    0.8
        971.0    404    7.2    0.2
        946.7    610    5.2   -1.8
     ...
    '''
sound_data = StringIO(data_txt)
p, h, T, Td = np.loadtxt(sound_data, unpack=True)
```
