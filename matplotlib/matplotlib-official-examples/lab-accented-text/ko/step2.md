# Unicode 문자 사용하기

Matplotlib 는 문자열에서 Unicode 문자를 직접 사용하는 것도 지원합니다.

```python
import matplotlib.pyplot as plt

# Unicode demo
fig, ax = plt.subplots()
ax.set_title("GISCARD CHAHUTÉ À L'ASSEMBLÉE")
ax.set_xlabel("LE COUP DE DÉ DE DE GAULLE")
ax.set_ylabel('André was here!')
ax.text(0.2, 0.8, 'Institut für Festkörperphysik', rotation=45)
ax.text(0.4, 0.2, 'AVA (check kerning)')

plt.show()
```
