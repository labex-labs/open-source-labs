# Clonar el repositorio de Git

Para comenzar a explorar las capacidades de filtrado por rango de fechas de Git, primero necesitamos un repositorio de Git con el que trabajar. Utilizaremos el repositorio `git-playground` proporcionado por LabEx.

Comencemos clonando el repositorio:

1. Abra su terminal en la máquina virtual (VM) de LabEx.

![terminal](../assets/screenshot-20250306-shbu3WrQ@2x.png)

2. Ejecute el siguiente comando para clonar el repositorio:

```bash
git clone https://github.com/labex-labs/git-playground
```

Debería ver una salida similar a esta:

```
Cloning into 'git-playground'...
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 8 (delta 0), reused 8 (delta 0), pack-reused 0
Receiving objects: 100% (8/8), done.
```

3. Navegue hasta el directorio del repositorio:

```bash
cd git-playground
```

Ahora que tenemos el repositorio en nuestra máquina local, podemos comenzar a explorar el historial de commits (confirmaciones).
