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

Si se trabaja desde el ZIP, basta con extraerlo, abrir la carpeta y ejecutar los
comandos de `py -m venv venv` en adelante.

## Base de datos y datos de prueba

El proyecto usa SQLite y no requiere instalar ningún servidor. La entrega incluye
la base de datos `db.sqlite3` ya creada, con las categorías, los lugares
patrimoniales y los usuarios de prueba, por lo que **no es necesario ejecutar
migraciones** para probar la aplicación.

Si se quiere crear la base desde cero:

```powershell
cd patrimonio_vivo
py manage.py migrate
py manage.py createsuperuser
```

Luego, desde http://127.0.0.1:8000/admin/ se agregan las categorías y los lugares
(Django Admin) y se crean los usuarios `editor` y `lector` según la sección
siguiente.

## Usuarios y permisos

La base de datos incluye tres usuarios de prueba. Las contraseñas no se publican
en el repositorio.

| Usuario | Permisos | Qué puede hacer |
|---|---|---|
| `admin` | Superusuario | Todo, incluido el Django Admin (`/admin/`) |
| `editor` | `Can add` y `Can change` de *lugar patrimonial* | Entrar a Gestión, agregar y editar lugares |
| `lector` | Ninguno | Entrar a Gestión, solo consultar |

Un visitante sin sesión puede ver inicio, catálogo, detalle y categorías.

### Crear los usuarios desde cero

1. Administrador: `py manage.py createsuperuser`.
2. Iniciar el servidor, entrar a `/admin/` con el administrador y en
   **Usuarios → Añadir usuario** crear `editor` y `lector` con una contraseña a elección.
3. En la ficha de `editor`, sección **Permisos de usuario**, asignar:
   - `core | lugar patrimonial | Can add lugar patrimonial`
   - `core | lugar patrimonial | Can change lugar patrimonial`
4. `lector` no lleva permisos. No es necesario marcar "Es staff" ni "Es superusuario".

## Ejecutar

```powershell
cd patrimonio_vivo
py manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Páginas principales

- `/` inicio, `/catalogo/` catálogo con filtro por categoría, `/detalle/<id>/` detalle y `/categorias/` categorías.
- `/login/` y `/logout/` para iniciar y cerrar sesión.
- `/gestion/` panel solo para usuarios con sesión iniciada.
- `/gestion/nuevo/` y `/gestion/<id>/editar/` requieren los permisos de agregar y modificar lugares. Sin ellos el sistema responde con un error 403, incluso escribiendo la URL.

Las categorías se administran desde Django Admin.