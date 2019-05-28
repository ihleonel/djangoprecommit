# Django Pre-Commit
## Dependencias
1. Python 3.6
1. Virtualenv 16.0.0
1. Git

## Como iniciar
1. Clonar repositorio
1. Crear entorno virtual `$ virtualenv --python=python3.6 env`
1. Iniciar entorno virtual `$ source env/bin/activate`
1. Instalar dependencias `$ pip install -r requirements.txt`
1. Instalar pre-commit `$ pre-commit install`

## Black
Si el pre-commit sugiere cambios se deberá correr black señalando la ruta del archivo a formatear:

`$ black path/to/file.py`

Una vez formateado se deberá correr el comando:

`$ git add -A`

Luego se deberá proceder haciendo el commit nuevamente.
