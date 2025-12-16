# 🚀 Guía de Despliegue en Render

## Pasos para Desplegar

### 1. Preparar el Repositorio en GitHub

1. **Inicializar Git** (si no lo has hecho):
   ```bash
   git init
   git add .
   git commit -m "Aplicación de registro de riegos lista para producción"
   ```

2. **Crear repositorio en GitHub**:
   - Ve a [GitHub](https://github.com/new)
   - Crea un nuevo repositorio (ej: `registro-riegos`)
   - **NO** inicialices con README (ya tienes uno)

3. **Conectar y subir**:
   ```bash
   git remote add origin https://github.com/TU_USUARIO/registro-riegos.git
   git branch -M main
   git push -u origin main
   ```

### 2. Desplegar en Render

1. **Ir a Render**:
   - Ve a [render.com](https://render.com)
   - Inicia sesión o crea cuenta (puedes usar GitHub)

2. **Crear nuevo Web Service**:
   - Click en "New +" → "Web Service"
   - Conecta tu repositorio de GitHub
   - Selecciona el repositorio `registro-riegos`

3. **Configurar el servicio**:
   - **Name**: `registro-riegos` (o el nombre que prefieras)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (o el que prefieras)

4. **Configurar Variables de Entorno**:
   En la sección "Environment Variables", agregar:
   
   | Key | Value |
   |-----|-------|
   | `SUPABASE_URL` | `https://xdegzbnuezoqxgqaqsqs.supabase.co` |
   | `SUPABASE_KEY` | Tu clave de Supabase (la que está en tu archivo .env) |

   > ⚠️ **IMPORTANTE**: Copia el valor de `SUPABASE_KEY` de tu archivo `.env` local

5. **Crear el servicio**:
   - Click en "Create Web Service"
   - Render comenzará a desplegar automáticamente
   - Espera 2-3 minutos

### 3. Verificar el Despliegue

Una vez completado:
- Render te dará una URL como: `https://registro-riegos.onrender.com`
- Abre esa URL en tu navegador
- Verifica que la aplicación funcione correctamente

### 4. Configuración Adicional (Opcional)

#### Dominio Personalizado
Si tienes un dominio propio:
1. Ve a Settings → Custom Domain
2. Agrega tu dominio
3. Configura los DNS según las instrucciones

#### Auto-Deploy
Render ya está configurado para auto-deploy:
- Cada vez que hagas `git push` a tu rama `main`
- Render desplegará automáticamente los cambios

## 📋 Checklist de Despliegue

- [ ] Código subido a GitHub
- [ ] Servicio creado en Render
- [ ] Variables de entorno configuradas
- [ ] Aplicación desplegada exitosamente
- [ ] Probada la URL de producción
- [ ] Verificado que Supabase se conecta correctamente
- [ ] Probado registro de riegos
- [ ] Probado resumen semanal
- [ ] Probado exportación a Excel

## 🔧 Troubleshooting

### Error: "Application failed to respond"
- Verifica que las variables de entorno estén configuradas
- Revisa los logs en Render Dashboard

### Error de conexión a Supabase
- Verifica que `SUPABASE_URL` y `SUPABASE_KEY` estén correctas
- Asegúrate de que Supabase esté activo

### La aplicación es lenta al inicio
- Render Free tier "duerme" después de 15 min de inactividad
- El primer request puede tardar 30-50 segundos
- Considera upgrade a plan de pago si necesitas respuesta inmediata

## 📱 Acceso Móvil

Una vez desplegado, tu equipo puede acceder desde cualquier dispositivo:
- Móviles: Abrir la URL en cualquier navegador
- Tablets: Misma URL
- Desktop: Misma URL

¡Listo para usar! 🎉
