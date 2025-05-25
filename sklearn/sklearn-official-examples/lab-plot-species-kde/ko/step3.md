# 데이터 준비

이제 커널 밀도 추정을 위해 데이터를 준비할 것입니다. 데이터셋에서 위도와 경도 정보를 추출하고 라디안으로 변환할 것입니다.

```python
Xtrain = np.vstack([data["train"]["dd lat"], data["train"]["dd long"]]).T
ytrain = np.array(
    [d.decode("ascii").startswith("micro") for d in data["train"]["species"]],
    dtype="int",
)
Xtrain *= np.pi / 180.0  # 위도/경도를 라디안으로 변환
```
