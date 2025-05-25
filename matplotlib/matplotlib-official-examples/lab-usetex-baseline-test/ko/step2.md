# Matplotlib 폰트 설정

Matplotlib 텍스트에 사용할 폰트를 설정해야 합니다. Computer Modern 폰트를 사용하고 이를 Matplotlib 의 기본 폰트로 설정합니다.

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```
