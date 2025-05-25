# `confidence_ellipse` 함수 정의

다음으로, 데이터셋의 x 및 y 좌표, 타원을 그릴 축 객체, 그리고 표준 편차의 개수를 입력으로 받는 `confidence_ellipse` 함수를 정의합니다. 이 함수는 타원을 나타내는 Matplotlib 패치 객체를 반환합니다.

```python
def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    *x*와 *y*의 공분산 신뢰 타원 플롯을 생성합니다.

    매개변수
    ----------
    x, y : array-like, shape (n, )
        입력 데이터.

    ax : matplotlib.axes.Axes
        타원을 그릴 축 객체.

    n_std : float
        타원의 반경을 결정하기 위한 표준 편차의 개수.

    **kwargs
        `~matplotlib.patches.Ellipse` 로 전달됨

    반환값
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensional dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the standard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the standard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)
```
