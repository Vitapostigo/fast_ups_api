# Dashboard UPS con FastAPI

Este proyecto es un **dashboard web para monitorizar un SAI (UPS) Salicru** usando Python y FastAPI. Permite visualizar en tiempo real datos principales, secundarios y adicionales del SAI de manera clara y responsiva, incluyendo porcentaje de batería, carga, voltaje, frecuencia y estado de la fuente de energía.

El proyecto incluye un **Dockerfile**, por lo que puede ejecutarse fácilmente en contenedores sin necesidad de instalar dependencias adicionales en el sistema host.

---

## Cómo usar

1. Descargar el Dockerfile y construir el contenedor 

docker build -t dashboard-ups .

    Ejecutar el contenedor:

sudo docker run --rm --network=host --name fastups_container fastups

Nota: Es necesario usar --network host para que la aplicación pueda acceder al puerto que expone el SAI en el PC.

Acceder desde el navegador:

http://localhost:18000/

El dashboard se actualizará automáticamente cada 2 segundos mostrando los datos del SAI.
Configuración del SAI

Para configurar el sistema se puede tomar esta guía de ejemplo: 
[Administración básica del SAI Salicru SPS One 900VA con NUT]
(https://www.jormc.es/tutoriales/administracion-basica-del-sai-salicru-spsone-900va-con-nut/#Introduccion)

La única diferencia recomendada es cambiar la parte de:

LISTEN 127.0.0.1 3493

por

LISTEN 0.0.0.0 3493

para permitir que NUT escuche en todas las interfaces y pueda ser accedido por la API.
