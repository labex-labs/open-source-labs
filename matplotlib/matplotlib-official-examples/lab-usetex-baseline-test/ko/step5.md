# 플롯 제한 및 레이블 설정

원하는 출력과 일치하도록 플롯 제한 및 레이블을 설정합니다.

```python
for ax in axs:
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[])
    ax.set_title(f"usetex={ax.usetex}\n")
```
