## Esquema


├── App/
│   ├── src/
│   │   ├── __init__.py 
│   │   └── signal.py              
│   ├── scripts/                
│   │   └── run.py                   
│   └── Signal.md                   
├── .gitignore                      
└── venv/

# 2. Definición de Componentes

1. (Capas del Sistema)
Esta sección define la responsabilidad principal de cada capa funcional dentro de tu arquitectura modular.

Capa de Lógica del Sistema (app/src/):

Responsabilidad: Define el comportamiento central del proyecto.

Función: Se encarga de la conexión serial, el parsing de datos y la visualización en tiempo real.

Capa de Control y Ejecución (app/scripts/):

Responsabilidad: Define el arranque robusto del sistema.

Función: Gestiona la configuración de rutas (sys.path), la detección automática de puerto y el control de errores en el inicio.

Capa de Encapsulación (app/):

Responsabilidad: Actúa como el contenedor principal del proyecto.

Función: Agrupa y organiza las capas funcionales (src/ y scripts/) para la entrega y la importación.

2. (Archivos Clave)
Esta sección define la tarea específica que realiza cada archivo o mecanismo dentro del código.

signal.py (Módulo de Clase):

Tarea: Implementa la Clase Signal para la adquisición de datos seriales y el método stream() para la gráfica en vivo.

run.py (Script de Ejecución):

Tarea: Es el punto de entrada del programa. Llama a la lógica e implementa la detección de puerto (detectar_puerto_serial).

__init__.py (Archivo de Configuración):

Tarea: Define la carpeta src/ como un paquete de Python, permitiendo la correcta importación por run.py.

Mecanismo try/finally (Estructura de Control):

Tarea: Asegura que el recurso del puerto serial (detector_senal.ser.close()) se cierre de forma segura en todo momento, evitando bloqueos.