# Autograde

Una herramienta CLI en Python que inspecciona un repositorio de GitHub y verifica si cumple con una serie de condiciones.

## Requisitos previos

- Python 3.14 o superior
- `uv` como gestor de dependencias (https://docs.astral.sh/uv/)

## Instalación

Clona el repositorio e instala las dependencias:

```bash
git clone <repository-url>
cd autograde
uv sync
```

## Uso

### Modo 1: Interactivo (Recomendado)

Ejecuta la herramienta sin argumentos y te pedirá el repositorio:

```bash
uv run python autograde.py
```

**Salida:**
```
============================================================
🔍 AUTOGRADE - GitHub Repository Validator
============================================================

📍 Enter the GitHub repository URL (format: https://github.com/owner/repo): https://github.com/microsoft/vscode

============================================================
📊 Checking repository: https://github.com/microsoft/vscode
============================================================

✅ 1. The project is a git repository: Yes
✅ 2. That the 'main' branch exists: Yes
✅ 3. That the 'feature' branch exists in remote: Yes
✅ 4. That the 'file1.txt' file exists in main: Yes

============================================================
✅ All conditions met! Repository is valid.
============================================================
```

### Modo 2: Con argumento (Línea de comandos)

Proporciona la URL completa del repositorio como parámetro:

```bash
uv run python autograde.py https://github.com/propietario/repositorio
```

**Ejemplo:**
```bash
uv run python autograde.py https://github.com/microsoft/vscode
```

### Obtener ayuda

```bash
uv run python autograde.py --help
```

## Condiciones verificadas

La herramienta verifica las siguientes 4 condiciones:

1. **✅ Es un repositorio git**: Siempre cumple para repositorios de GitHub
2. **✅ La rama "main" existe**: Verifica que exista una rama llamada "main"
3. **✅ La rama "feature" existe**: Verifica que exista una rama llamada "feature" en el repositorio remoto
4. **✅ El archivo "file1.txt" existe**: Verifica que exista un archivo llamado "file1.txt" en la rama main

Todas las condiciones deben cumplirse para que el repositorio sea válido.

## Ejemplos de uso

### Ejemplo 1: Repositorio válido

```bash
$ uv run python autograde.py https://github.com/microsoft/vscode
```

Si cumple todas las condiciones, verás:
```
✅ All conditions met! Repository is valid.
```

### Ejemplo 2: Repositorio inválido

```bash
$ uv run python autograde.py https://github.com/google/chrome
```

Si falta alguna condición, verás todas revisadas (incluso las posteriores a la que falla):
```
✅ 1. The project is a git repository: Yes
✅ 2. That the 'main' branch exists: Yes
❌ 3. That the 'feature' branch exists in remote: No
✅ 4. That the 'file1.txt' file exists in main: Yes

❌ Some conditions not met.
```

**Nota**: La herramienta revisa **todas las 4 condiciones** sin detenerse, así que obtendrás un reporte completo incluso si una falla.

## Pruebas

Ejecuta las pruebas unitarias:

```bash
uv run pytest
```

Para ver más detalles de las pruebas:

```bash
uv run pytest -v
```

## Dependencias

- **pygithub**: Para acceder a la API de GitHub
- **pytest**: Para ejecutar las pruebas (desarrollo)
