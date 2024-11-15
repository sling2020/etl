# ETL Films2: Procesamiento Escalable de Datos

## Descripción del Proyecto
Este proyecto implementa ETL (Extract, Transform, Load) para procesar el archivo `Films2.xlsx`. El objetivo es transformar los datos del modelo entidad-relación en un formato estructurado y procesable, utilizando pandas para garantizar la integridad de los datos y evitar valores dañados o erróneos.

## Detalles de la implementación
En este proyecto se usó una arquitectura basada en servicios con la finalidad de delegar las responsabilidades a los services que corresponda de tal forma que permita facilmente detectar el componente escífico de
README con el detalle de implementación y justificación de diseño y un informe cuyo
contenido se detalla más adelante. Esto se debe entregar en un repositorio git a elección.

## Estructura del Proyecto
El proyecto está construido sobre cuatro servicios principales, cada uno con una responsabilidad específica y un enfoque en la reusabilidad y escalabilidad:

**`data_base_service`**  
  Encargado de todas las interacciones con la base de datos, incluyendo:
  - Conexión y configuración de la base de datos.
  - Carga de registros a base de datos.

**`data_frame_service`**  
  Proporciona utilidades para manipular DataFrames de forma genérica:
  - Limpieza de datos según tipo de datos por columna.
  - Aplicación de transformaciones comunes a datasets.

**`data_frames_builder`**  
  Construye y prepara los DataFrames a partir de diferentes fuentes de datos:
  - Soporte para múltiples formatos [Por ahora solo Excel (`Films2.xlsx`)].

**`data_set_service`**  
  Coordina el flujo de datos a lo largo de todo el ETL:
  - Orquestación de la extracción, transformación y carga.
  - Adaptación de las operaciones según las características de cada dataset [Por ahora solo (`Films2`)].
  - Generación de reportes de salida con los resultados finales.