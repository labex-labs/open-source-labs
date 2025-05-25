# 데이터 저장 및 로드

Pandas 는 csv, excel, hdf5 등 다양한 형식으로 데이터를 저장하고 로드하는 메서드를 제공합니다.

```python
# 데이터를 csv 파일로 저장
df.to_csv("foo.csv")

# 데이터를 csv 파일에서 로드
pd.read_csv("foo.csv")
```
