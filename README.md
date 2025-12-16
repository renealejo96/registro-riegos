# Registro de Riegos - Finca

Aplicación web para el registro diario de riegos en módulos de la finca.

## Características

- 📱 Interfaz responsive (móvil y desktop)
- 💧 Registro de riego por Agua o Comida (Fertilizante)
- 📊 Visualización de registros del día
- 📜 Historial completo de riegos
- 🔍 Búsqueda y filtrado
- ☁️ Base de datos en la nube con Supabase

## Configuración de Supabase

### 1. Crear tabla en Supabase

Ejecuta este SQL en el editor SQL de Supabase:

```sql
-- Crear tabla de riegos
CREATE TABLE riegos (
    id BIGSERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    modulo TEXT NOT NULL,
    tipo_riego TEXT NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

-- Crear índices para mejorar el rendimiento
CREATE INDEX idx_riegos_fecha ON riegos(fecha);
CREATE INDEX idx_riegos_timestamp ON riegos(timestamp);

-- Habilitar Row Level Security (RLS)
ALTER TABLE riegos ENABLE ROW LEVEL SECURITY;

-- Crear política para permitir todas las operaciones (ajusta según tus necesidades)
CREATE POLICY "Permitir todo acceso" ON riegos
    FOR ALL
    USING (true)
    WITH CHECK (true);
```

### 2. Obtener credenciales

1. Ve a tu proyecto en Supabase
2. Settings > API
3. Copia:
   - Project URL (SUPABASE_URL)
   - anon/public key (SUPABASE_KEY)

### 3. Configurar variables de entorno

Crea un archivo `.env`:

```bash
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu-clave-anon-key
SECRET_KEY=una-clave-secreta-segura
```

## Instalación Local

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Ejecutar aplicación
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## Despliegue en Render

### 1. Preparar el repositorio

```bash
git init
git add .
git commit -m "Initial commit"
```

Sube tu código a GitHub/GitLab

### 2. Configurar en Render

1. Ve a [render.com](https://render.com)
2. New > Web Service
3. Conecta tu repositorio
4. Configuración:
   - **Name**: riegos-app (o el nombre que prefieras)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### 3. Variables de entorno en Render

En la configuración del Web Service, añade:

- `SUPABASE_URL`: Tu URL de Supabase
- `SUPABASE_KEY`: Tu clave de Supabase
- `SECRET_KEY`: Una clave secreta segura
- `FLASK_ENV`: production

### 4. Deploy

Render desplegará automáticamente tu aplicación. ¡Listo!

## Uso

1. **Registrar riego**:
   - Selecciona tipo de riego (Agua o Comida)
   - Marca los módulos regados
   - Click en "Registrar Riego"

2. **Ver historial**:
   - Click en "Ver Historial"
   - Usa la búsqueda para filtrar

3. **Registros del día**:
   - Se actualizan automáticamente en la página principal

## Estructura del Proyecto

```
REG_RIEGOS/
├── app.py                 # Aplicación Flask principal
├── modulos.csv           # Lista de módulos
├── requirements.txt      # Dependencias
├── .env.example         # Ejemplo de variables de entorno
├── .gitignore           # Archivos a ignorar en git
├── README.md            # Este archivo
├── templates/           # Plantillas HTML
│   ├── index.html
│   └── historial.html
└── static/             # Archivos estáticos
    └── css/
        └── styles.css
```

## Tecnologías

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Base de datos**: Supabase (PostgreSQL)
- **Deploy**: Render
- **Icons**: Font Awesome

## Personalización

### Agregar/modificar módulos

Edita el archivo `modulos.csv`:

```csv
modulo
11
12
13
...
```

### Cambiar colores

Edita las variables CSS en `static/css/styles.css`:

```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #10b981;
    ...
}
```

## Soporte

Para problemas o sugerencias, crea un issue en el repositorio.

## Licencia

MIT
