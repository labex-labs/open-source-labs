# DataFrame 생성

Pandas 의 데이터는 DataFrame 에 저장됩니다. DataFrame 은 잠재적으로 서로 다른 유형의 열을 가진 2 차원 레이블 데이터 구조입니다.

```python
# DataFrame 생성
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
```
