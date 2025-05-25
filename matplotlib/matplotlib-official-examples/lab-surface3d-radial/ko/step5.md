# 제한 조정 및 레이블 추가

마지막으로, Matplotlib 의 `set_zlim()` 및 `set_xlabel()`, `set_ylabel()`, `set_zlabel()` 함수를 사용하여 플롯의 제한을 조정하고 축 레이블을 추가합니다. 또한 LaTeX 수학 모드 (math mode) 를 사용하여 축 레이블을 작성합니다.

```python
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
```
