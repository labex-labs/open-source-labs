# 랜덤 시드 및 Bin 설정

재현성을 위해 랜덤 시드를 설정하고 bin 경계를 고정합니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Fixing bin edges
HIST_BINS = np.linspace(-4, 4, 100)
```
