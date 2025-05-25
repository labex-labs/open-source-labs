# 별칭 (Aliases)

대화형 모드에서 키 입력을 줄이기 위해, 여러 속성에는 짧은 별칭이 있습니다. 예를 들어, 'linewidth'에 대한 'lw'와 'markeredgecolor'에 대한 'mec'가 있습니다. 인트로스펙션 모드에서 set 또는 get 을 호출할 때, 이러한 속성은 'fullname' 또는 'aliasname'으로 나열됩니다.

```python
l1, l2 = plt.plot([1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5])
plt.setp(l1, linewidth=2, color='r')
plt.setp(l2, linewidth=1, color='g')
```
