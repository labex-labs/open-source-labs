# Figure 생성

이 단계에서는 두 개의 서브플롯 (subplot) 을 가진 figure 를 생성합니다. 첫 번째 서브플롯은 2D 플롯이고, 두 번째 서브플롯은 3D 플롯입니다.

```python
fig = plt.figure(figsize=plt.figaspect(2.))
fig.suptitle('A Tale of 2 Subplots')
```
