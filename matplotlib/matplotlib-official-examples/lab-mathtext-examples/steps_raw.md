# Matplotlib Math Rendering Engine Lab

## Introduction

This lab will guide you to create a figure that showcases the selected features of Matplotlib's math rendering engine. The figure will demonstrate how to write mathematical expressions with examples of subscripts, superscripts, fractions, binomials, stacked numbers, radicals, fonts, accents, Greek, Hebrew, delimiters, functions, and symbols.

## Steps

### Step 1: Import libraries

In this step, we will import the required libraries for this lab.

```python
import matplotlib.pyplot as plt
```

### Step 2: Set up the demo examples

In this step, we will set up the demo examples of math expressions that we will showcase in the figure.

```python
mathtext_demos = {
    "Header demo":
        r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = "
        r"U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} "
        r"\int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ "
        r"U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_"
        r"{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$",

    "Subscripts and superscripts":
        r"$\alpha_i > \beta_i,\ "
        r"\alpha_{i+1}^j = {\rm sin}(2\pi f_j t_i) e^{-5 t_i/\tau},\ "
        r"\ldots$",

    "Fractions, binomials and stacked numbers":
        r"$\frac{3}{4},\ \binom{3}{4},\ \genfrac{}{}{0}{}{3}{4},\ "
        r"\left(\frac{5 - \frac{1}{x}}{4}\right),\ \ldots$",

    "Radicals":
        r"$\sqrt{2},\ \sqrt[3]{x},\ \ldots$",

    "Fonts":
        r"$\mathrm{Roman}\ , \ \mathit{Italic}\ , \ \mathtt{Typewriter} \ "
        r"\mathrm{or}\ \mathcal{CALLIGRAPHY}$",

    "Accents":
        r"$\acute a,\ \bar a,\ \breve a,\ \dot a,\ \ddot a, \ \grave a, \ "
        r"\hat a,\ \tilde a,\ \vec a,\ \widehat{xyz},\ \widetilde{xyz},\ "
        r"\ldots$",

    "Greek, Hebrew":
        r"$\alpha,\ \beta,\ \chi,\ \delta,\ \lambda,\ \mu,\ "
        r"\Delta,\ \Gamma,\ \Omega,\ \Phi,\ \Pi,\ \Upsilon,\ \nabla,\ "
        r"\aleph,\ \beth,\ \daleth,\ \gimel,\ \ldots$",

    "Delimiters, functions and Symbols":
        r"$\coprod,\ \int,\ \oint,\ \prod,\ \sum,\ "
        r"\log,\ \sin,\ \approx,\ \oplus,\ \star,\ \varpropto,\ "
        r"\infty,\ \partial,\ \Re,\ \leftrightsquigarrow, \ \ldots$",
}
```

### Step 3: Create the figure and axis

In this step, we will create the figure and axis for the math expression examples.

```python
# Creating figure and axis.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0.01, 0.01, 0.98, 0.90],
                  facecolor="white", frameon=True)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Matplotlib's math rendering engine",
             color=mpl_grey_rgb, fontsize=14, weight='bold')
ax.set_xticks([])
ax.set_yticks([])
```

### Step 4: Define the line spacing

In this step, we will define the gap between lines in axes coords.

```python
n_lines = len(mathtext_demos)
line_axesfrac = 1 / n_lines
```

### Step 5: Plot the header demonstration formula

In this step, we will plot the header demonstration formula.

```python
full_demo = mathtext_demos['Header demo']
ax.annotate(full_demo,
            xy=(0.5, 1. - 0.59 * line_axesfrac),
            color='tab:orange', ha='center', fontsize=20)
```

### Step 6: Plot the feature demonstration formulae

In this step, we will plot the feature demonstration formulae.

```python
for i_line, (title, demo) in enumerate(mathtext_demos.items()):
    if i_line == 0:
        continue

    baseline = 1 - i_line * line_axesfrac
    baseline_next = baseline - line_axesfrac
    fill_color = ['white', 'tab:blue'][i_line % 2]
    ax.axhspan(baseline, baseline_next, color=fill_color, alpha=0.2)
    ax.annotate(f'{title}:',
                xy=(0.06, baseline - 0.3 * line_axesfrac),
                color=mpl_grey_rgb, weight='bold')
    ax.annotate(demo,
                xy=(0.04, baseline - 0.75 * line_axesfrac),
                color=mpl_grey_rgb, fontsize=16)
```

### Step 7: Display the figure

In this step, we will display the figure.

```python
plt.show()
```

## Summary

This lab has demonstrated how to create a figure that showcases the selected features of Matplotlib's math rendering engine. The figure demonstrated how to write mathematical expressions with examples of subscripts, superscripts, fractions, binomials, stacked numbers, radicals, fonts, accents, Greek, Hebrew, delimiters, functions, and symbols.
