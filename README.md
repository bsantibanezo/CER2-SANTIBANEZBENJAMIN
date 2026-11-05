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

## Base de datos y datos de prueba

El proyecto usa SQLite y no requiere instalar ningún servidor. La base de datos
no se incluye en el repositorio: se crea con los siguientes comandos.

```powershell
cd patrimonio_vivo
py manage.py migrate
py -X utf8 manage.py loaddata datos_iniciales
```

- `migrate` crea las tablas y los permisos de Django.
- `loaddata` carga las categorías y los lugares patrimoniales de prueba desde
  `core/fixtures/datos_iniciales.json`. El parámetro `-X utf8` asegura que las
  tildes se carguen correctamente en Windows.

## Configuración de usuarios y permisos

Las contraseñas no se publican en el repositorio. Cada usuario se crea al
configurar el proyecto.

**1. Administrador** (todos los permisos):

```powershell
py manage.py createsuperuser
```

**2. Editor y lector.** Iniciar el servidor (ver sección siguiente), entrar a
http://127.0.0.1:8000/admin/ con el administrador y en **Usuarios → Añadir
usuario** crear:

| Usuario | Permisos de usuario a asignar (en su ficha, sección "Permisos") |
|---|---|
| `editor` | `core | lugar patrimonial | Can add lugar patrimonial` y `Can change lugar patrimonial` |
| `lector` | Ninguno |

Para ambos, definir una contraseña a elección. No es necesario marcar "Es staff"
ni "Es superusuario".

### Qué puede hacer cada usuario

| Usuario | Qué puede hacer |
|---|---|
| Visitante (sin sesión) | Ver inicio, catálogo, detalle y categorías |
| `admin` | Todo, incluido el Django Admin (`/admin/`) |
| `editor` | Entrar a Gestión, agregar y editar lugares |
| `lector` | Entrar a Gestión, solo consultar |

## Ejecutar

```powershell
py manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Páginas principales

- `/` inicio, `/catalogo/` catálogo con filtro por categoría, `/detalle/<id>/` detalle y `/categorias/` categorías.
- `/login/` y `/logout/` para iniciar y cerrar sesión.
- `/gestion/` panel solo para usuarios con sesión iniciada.
- `/gestion/nuevo/` y `/gestion/<id>/editar/` requieren los permisos de agregar y modificar lugares. Sin ellos el sistema responde con un error 403, incluso escribiendo la URL.

Las categorías se administran desde Django Admin.