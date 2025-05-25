# 바닥에 LaTeX 수식 쓰기

`text3d` 함수를 사용하여 3D 플롯의 z=0 '바닥'에 LaTeX 수식을 작성합니다.

```python
text3d(ax, (1, 5, 0),
       r"$\displaystyle G_{\mu\nu} + \Lambda g_{\mu\nu} = "
       r"\frac{8\pi G}{c^4} T_{\mu\nu}  $",
       zdir="z", size=1, usetex=True,
       ec="none", fc="k")
```
