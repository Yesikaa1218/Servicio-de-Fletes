# Servicio de Fletes

Este repositorio contiene los archivos y el código backend necesarios para implementar un servicio de fletes. La estructura del proyecto está diseñada para facilitar la gestión de choferes, vehículos, rutas y usuarios a través de una base de datos MongoDB.

## Archivos del Proyecto

- **backend.py**: Código principal que se encarga de la conexión con la base de datos y la gestión de los datos relacionados con choferes, vehículos, y rutas.
- **choferes.txt**: Archivo de texto que contiene información sobre los choferes en el siguiente formato:
- **rutas.txt**: Información sobre las rutas disponibles, incluyendo origen, destino y distancia
- **usuarios.txt**: Datos de los usuarios del servicio, que pueden incluir detalles como nombre y contacto.
- **vehiculos.txt**: Información sobre los vehículos disponibles para el servicio, incluyendo marca, modelo y disponibilidad.

## Estructura de la Base de Datos

El backend utiliza MongoDB para almacenar la información. Las siguientes colecciones están disponibles en la base de datos:

- **CLIENTES**: Información sobre los clientes que utilizan el servicio.
- **CONDUCTOR**: Datos de los choferes registrados.
- **ENVIO**: Información sobre los envíos realizados.
- **FACTURA**: Detalles de las facturas generadas.
- **OPINION**: Comentarios y valoraciones de los clientes.
- **SEGUIMIENTO**: Estado de los envíos.
- **TARIFA**: Tarifas por los diferentes servicios de fletes.
- **TRANSPORTE**: Datos relacionados con el transporte de mercancías.

## Tecnologías Usadas

- Python
- Tkinter (para la interfaz gráfica, si se aplica)
- PyMongo (para la conexión con MongoDB)

## Instrucciones para Usar

1. **Clonar el repositorio**:
 ```bash
 git clone <URL del repositorio>
 cd servicio-de-fletes
