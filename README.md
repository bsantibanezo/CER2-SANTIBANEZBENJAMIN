# Patrimonio Vivo

Catálogo digital de lugares patrimoniales de la Fundación Patrimonio Vivo.

Certamen N°2 · EIN082B Taller Lenguaje de Programación · Python y Django.

## Requisitos

- Python 3.12 o superior
- Git

## Instalación

```powershell
git clone https://github.com/bsantibanezo/CER2-SANTIBANEZBENJAMIN.git
cd CER2-SANTIBANEZBENJAMIN

py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
```

## Base de datos

El proyecto usa SQLite (`db.sqlite3`) y no requiere instalar ningún servidor. El repositorio ya incluye la base con categorías, lugares y usuarios de prueba.

Para crearla desde cero:

```powershell
cd patrimonio_vivo
py manage.py migrate
py manage.py createsuperuser
```

## Ejecutar

```powershell
cd patrimonio_vivo
py manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Usuarios de prueba

| Usuario | Contraseña | Qué puede hacer |
|---|---|---|
| admin | TU-CONTRASEÑA-ADMIN | Todo, incluido el Django Admin (`/admin/`) |
| editor | Patrimonio26 | Entrar a Gestión, agregar y editar lugares |
| lector | Patrimonio26 | Entrar a Gestión, solo consultar |

## Páginas principales

- `/` inicio, `/catalogo/` catálogo con filtro por categoría, `/detalle/<id>/` detalle y `/categorias/` categorías.
- `/login/` y `/logout/` para iniciar y cerrar sesión.
- `/gestion/` panel solo para usuarios con sesión iniciada.
- `/gestion/nuevo/` y `/gestion/<id>/editar/` requieren los permisos de agregar y modificar lugares. Sin ellos el sistema responde con un error 403, incluso escribiendo la URL.

Las categorías se administran desde Django Admin.
