# Sistema CRM - Gestión de Relaciones con Clientes

## Descripción
Sistema de gestión de relaciones con clientes (CRM) desarrollado en Python que permite administrar clientes y sus facturas asociadas. El sistema incluye funcionalidades para registrar clientes, crear facturas, realizar búsquedas y generar reportes financieros.

## Estructura del Proyecto
```
crm-system/
│
├── main.py              # Archivo principal para ejecutar el sistema
├── models.py            # Clases Cliente y Factura
├── validators.py        # Clase Validador para validaciones
├── crm_system.py        # Clase principal CRMSystem
├── requirements.txt     # Dependencias del proyecto
├── README.md           # Este archivo
├── cliente.json       # Base de datos de cliente (se crea automáticamente)
└── facturas.json       # Base de datos de facturas (se crea automáticamente)
```

## Características

### Gestión de Cliente
- Registro de nuevos cliente con validación de datos
- Búsqueda por email o nombre
- Visualización de lista completa de cliente
- Validación de formato de email
- Control de emails únicos

### Gestión de Facturas
- Creación de facturas asociadas a cliente
- Estados de factura: Pendiente, Pagada, Cancelada
- Visualización de facturas por cliente
- Numeración automática de facturas

### Reportes
- Resumen financiero por cliente
- Totales del sistema
- Ingresos recibidos vs pendientes

### Persistencia de Datos
- Almacenamiento en archivos JSON
- Carga automática al iniciar
- Guardado automático tras cada operación

## Instalación

1. **Clonar o descargar los archivos del proyecto**
    ```bash
       git clone https://github.com/denislcian/CRM_SYSTEM.git
       cd CRM_SYSTEM
    ```
## Uso

### Ejecutar el sistema:
```bash
python main.py
```

### Menú principal:
1. **Registrar nuevo cliente** - Añadir nuevos clientes al sistema
2. **Buscar cliente** - Localizar cliente por email o nombre
3. **Crear factura para cliente** - Generar facturas asociadas a clientes
4. **Mostrar todos los cliente** - Ver lista completa de cliente registrados
5. **Mostrar facturas de un cliente** - Ver facturas específicas de un cliente
6. **Resumen financiero por cliente** - Ver reportes de ingresos y estadísticas
7. **Salir** - Cerrar el sistema guardando los datos

## Validaciones Implementadas

### Email
- Formato válido usando expresiones regulares
- Verificación de unicidad en el sistema

### Campos Obligatorios
- Nombre y apellidos no pueden estar vacíos
- Email es requerido
- Descripción de factura es obligatoria

### Montos
- Solo acepta números positivos
- Validación de formato numérico

## Estructura de Datos

### Cliente
```python
{
    "id_cliente": "USR001",
    "nombre": "Juan",
    "apellidos": "Pérez García",
    "email": "juan.perez@email.com",
    "telefono": "123456789",
    "direccion": "Calle Principal 123",
    "fecha_registro": "24/06/2025",
    "facturas": ["FAC001", "FAC002"]
}
```

### Factura
```python
{
    "numero_factura": "FAC001",
    "id_cliente": "USR001", 
    "descripcion": "Servicio de consultoría",
    "monto": 500.00,
    "fecha_emision": "24/06/2025 14:30",
    "estado": "Pendiente"
}
```

## Funcionalidades Detalladas

### 1. Registro de cliente
- Solicita datos básicos: nombre, apellidos, email
- Datos opcionales: teléfono, dirección
- Genera ID automático (USR001, USR002, etc.)
- Registra fecha de alta automáticamente

### 2. Búsqueda de cliente
- **Por email**: Búsqueda exacta
- **Por nombre**: Búsqueda parcial en nombre, apellidos o nombre completo
- Muestra información detallada del cliente encontrado

### 3. Creación de Facturas
- Busca cliente por email
- Solicita descripción del servicio/producto
- Valida monto numérico positivo
- Permite seleccionar estado inicial
- Genera número de factura automático (FAC001, FAC002, etc.)

### 4. Reportes
- **Lista de cliente**: Muestra todos los cliente registrados
- **Facturas por cliente**: Detalle de facturas de un cliente específico
- **Resumen financiero**: Estadísticas completas del sistema

## Archivos de Datos

El sistema crea automáticamente dos archivos JSON:

- **cliente.json**: Base de datos de cliente
- **facturas.json**: Base de datos de facturas

Estos archivos se crean automáticamente la primera vez que se ejecuta el sistema y se actualizan con cada operación.

## Requisitos del Sistema

- **Python 3.6 o superior**
- **Librerías estándar de Python** (json, os, re, datetime, typing)
- **No requiere instalación de dependencias externas**

## Manejo de Errores

- Validación de entrada de datos
- Manejo de archivos inexistentes
- Control de errores de formato JSON
- Manejo de interrupciones por teclado (Ctrl+C)

## Ejemplos de Uso

### Registrar un cliente:
1. Ejecutar `python main.py`
2. Seleccionar opción 1
3. Completar los datos solicitados
4. El sistema asigna ID automáticamente

### Crear una factura:
1. Seleccionar opción 3
2. Ingresar email del cliente existente
3. Completar descripción y monto
4. Seleccionar estado de la factura

### Generar reporte financiero:
1. Seleccionar opción 6
2. El sistema muestra resumen por cliente y totales generales

## Notas Técnicas

- Los IDs se generan secuencialmente y se mantienen únicos
- Las fechas se almacenan en formato DD/MM/YYYY
- Los montos se manejan con precisión de 2 decimales
- El sistema es resistente a interrupciones y guarda datos automáticamente

## Posibles Mejoras Futuras

- Interfaz gráfica (GUI)
- Base de datos SQL
- Autenticación de cliente
- Exportación de reportes a PDF/Excel
- API REST para integración con otros sistemas
- Notificaciones automáticas de facturas vencidas