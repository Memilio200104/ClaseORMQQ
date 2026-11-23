# Portafolio de Proyectos — Clase ORM (versión alumnos)

Proyecto de práctica para la clase de **ORM de Django, creación de modelos y migraciones**.
La temática es un "Portafolio de Proyectos" sencillo construido con Django 5.1+, MySQL y Bootstrap 5.

## Requisitos previos

- Python 3.10 o superior
- MySQL Server en ejecución (local)
- Git

## Puesta en marcha

### 1. Clonar el repositorio

```bash
git clone https://github.com/Memilio200104/ClaseORMQQ.git
cd ClaseORMQQ
```

### 2. Crear y activar el entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

> Si PowerShell bloquea el script, ejecuta una vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

**Windows (CMD):**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Mac / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

Sabrás que está activo porque la terminal mostrará `(venv)` al inicio.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> **Mac:** si falla la instalación de `mysqlclient`, instala primero
> `brew install mysql pkg-config`.
> **Linux (Debian/Ubuntu):** `sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config`.

### 4. Crear la base de datos en MySQL

Entra a MySQL (consola, MySQL Workbench, etc.) y ejecuta:

```sql
CREATE DATABASE clase_orm_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. Configurar las variables de entorno

Copia el archivo de ejemplo:

**Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

**Mac / Linux:**

```bash
cp .env.example .env
```

Abre `.env` y reemplaza `DB_USER` y `DB_PASSWORD` con tus credenciales locales de MySQL.

### 6. Probar que el servidor arranca

```bash
python manage.py runserver
```

Abre <http://127.0.0.1:8000/> en el navegador.

> En este punto aún no hay migraciones, por eso Django mostrará un aviso de
> "unapplied migrations". Es normal: lo resolveremos juntos en la clase.

## Lo que haremos en clase

1. **Modelos:** completar el modelo `Proyecto` en `proyectos/models.py` (busca los `# TODO`).
2. **Migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. **Admin:** registrar el modelo en `proyectos/admin.py` y crear un superusuario:
   ```bash
   python manage.py createsuperuser
   ```
4. **ORM:** reemplazar los valores de ejemplo en `proyectos/views.py` por consultas reales.
5. **Template:** completar las tarjetas en `proyectos/templates/proyectos/lista.html` (busca el `TODO`).

## Estructura del proyecto

```
ClaseORMQQ/
├── config/                 # Configuración del proyecto (settings, urls)
├── proyectos/              # App principal
│   ├── models.py           # Modelo Proyecto
│   ├── views.py            # Vista lista_proyectos (consultas ORM)
│   ├── admin.py            # Registro en el panel de administración
│   ├── urls.py
│   └── templates/proyectos/lista.html
├── .env.example
├── requirements.txt
└── manage.py
```
