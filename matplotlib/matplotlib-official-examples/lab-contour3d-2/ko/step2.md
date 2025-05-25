# 데이터 생성

다음으로, 등고선 플롯을 생성하는 데 사용할 데이터를 생성해야 합니다. `mpl_toolkits.mplot3d` 모듈의 `get_test_data()` 함수를 사용하여 샘플 데이터를 생성합니다.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
