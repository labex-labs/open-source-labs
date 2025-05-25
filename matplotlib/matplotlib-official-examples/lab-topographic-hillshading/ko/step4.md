# 광원 및 컬러맵 지정

광원의 방위각 (azimuth) 과 고도 (altitude) 를 설정하여 `LightSource` 객체를 지정합니다. 또한 플롯에 사용할 컬러맵 (colormap) 을 설정합니다.

```python
ls = LightSource(azdeg=315, altdeg=45)
cmap = plt.cm.gist_earth
```
