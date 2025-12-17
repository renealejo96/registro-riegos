-- Script para actualizar la tabla de riegos con los nuevos campos
-- Ejecutar en Supabase SQL Editor

-- Agregar columna para sistema de riego (ducha o goteo)
ALTER TABLE riegos 
ADD COLUMN IF NOT EXISTS sistema_riego VARCHAR(10);

-- Agregar columna para tiempo en minutos
ALTER TABLE riegos 
ADD COLUMN IF NOT EXISTS tiempo_minutos INTEGER;

-- Actualizar registros existentes con valores por defecto
UPDATE riegos 
SET sistema_riego = 'N/A', tiempo_minutos = 0
WHERE sistema_riego IS NULL OR tiempo_minutos IS NULL;

-- Ver estructura actualizada
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'riegos'
ORDER BY ordinal_position;
