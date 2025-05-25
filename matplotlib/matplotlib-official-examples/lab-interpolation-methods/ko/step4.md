# 서브플롯 생성

보간 방법을 사용하여 이미지를 표시하기 위해 서브플롯을 생성합니다.

```python
fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(9, 6),
                        subplot_kw={'xticks': [], 'yticks': []})
```
