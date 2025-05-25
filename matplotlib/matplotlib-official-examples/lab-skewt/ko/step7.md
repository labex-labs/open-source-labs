# 데이터 준비

SkewT-logP 다이어그램에 사용할 데이터를 준비합니다. StringIO 모듈을 사용하여 문자열에서 데이터를 읽고, NumPy 를 사용하여 배열로 로드합니다.

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
