# figure 와 subplot 생성

다음으로, 데이터를 표시하기 위해 figure 와 subplot 을 생성합니다. 확대된 삽입의 두 가지 다른 예시를 나란히 표시하기 위해 두 개의 subplot 을 생성합니다.

```python
fig, (ax, ax2) = plt.subplots(ncols=2, figsize=[6, 3])
```
