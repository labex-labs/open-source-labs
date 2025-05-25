# 클린 논리 연산 (Kleene logical operations)

Pandas 는 `&` (and), `|` (or), `^` (exclusive-or) 와 같은 논리 연산에 대해 클린 논리 (3 값 논리, three-value logic) 를 구현합니다. 이는 `np.nan`이 논리 연산에서 동작하는 방식과 다릅니다.

```python
# np.nan 과 NA 의 'or' 연산 차이 시연
pd.Series([True, False, np.nan], dtype="object") | True # np.nan 은 다르게 동작함
pd.Series([True, False, pd.NA], dtype="boolean") | True # NA 는 클린 논리를 따름

# np.nan 과 NA 의 'and' 연산 차이 시연
pd.Series([True, False, np.nan], dtype="object") & True # np.nan 은 다르게 동작함
pd.Series([True, False, pd.NA], dtype="boolean") & True # NA 는 클린 논리를 따름
```
