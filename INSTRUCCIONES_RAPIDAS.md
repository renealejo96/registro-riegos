# 📋 INSTRUCCIONES RÁPIDAS DE DESPLIEGUE

## 1. Subir a GitHub (5 minutos)

```bash
# Ya hiciste el commit, ahora:

# 1. Crea un repositorio en GitHub
# Ve a: https://github.com/new
# Nombre sugerido: registro-riegos
# NO marques "Initialize with README"

# 2. Conecta tu repositorio local (reemplaza TU_USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/registro-riegos.git
git branch -M main
git push -u origin main
```

## 2. Desplegar en Render (10 minutos)

### Paso 1: Crear cuenta y conectar GitHub
1. Ve a [render.com](https://render.com)
2. Sign up → Conecta con GitHub
3. Autoriza Render a acceder a tus repositorios

### Paso 2: Crear Web Service
1. Click "New +" → "Web Service"
2. Busca y selecciona `registro-riegos`
3. Click "Connect"

### Paso 3: Configurar el servicio
```
Name: registro-riegos
Environment: Python 3
Region: Oregon (US West) o el más cercano
Branch: main
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Instance Type: Free
```

### Paso 4: Variables de Entorno ⚠️ IMPORTANTE
Click en "Advanced" y agrega estas variables:

```
SUPABASE_URL
https://xdegzbnuezoqxgqaqsqs.supabase.co

SUPABASE_KEY
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhkZWd6Ym51ZXpvcXhncWFxc3FzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjU4MjEzNjQsImV4cCI6MjA4MTM5NzM2NH0.E1VtnPB5CNaZG6IsmFmBgjwXX8PK-ijiZGAHF3wVfgs
```

### Paso 5: Desplegar
1. Click "Create Web Service"
2. Espera 2-3 minutos (verás logs en tiempo real)
3. ✅ Cuando veas "Your service is live", ¡está listo!

## 3. Probar la Aplicación

Tu URL será algo como:
```
https://registro-riegos.onrender.com
```

Render te la mostrará en la parte superior del dashboard.

## 🎉 ¡Listo!

Ahora puedes:
- Compartir la URL con tu equipo
- Acceder desde cualquier móvil/tablet
- Los registros se guardan automáticamente en Supabase

## 🔄 Actualizar en el Futuro

Cada vez que hagas cambios:
```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

Render detectará los cambios y desplegará automáticamente (toma ~2 min).

## ⚠️ Nota Importante sobre el Plan Free

- El servidor "duerme" después de 15 minutos sin uso
- La primera carga después de dormir toma 30-50 segundos
- Esto es normal en el plan gratuito
- Si necesitas respuesta instantánea, considera el plan de pago ($7/mes)

## 📞 Soporte

Si algo no funciona:
1. Revisa los logs en Render Dashboard
2. Verifica que las variables de entorno estén correctas
3. Asegúrate que Supabase esté activo
