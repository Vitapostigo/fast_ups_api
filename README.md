# Dashboard UPS con FastAPI

Este proyecto es un **dashboard web para monitorizar un SAI (UPS) Salicru** usando Python y FastAPI. Permite visualizar en tiempo real datos principales, secundarios y adicionales del SAI de manera clara y responsiva, incluyendo porcentaje de batería, carga, voltaje, frecuencia y estado de la fuente de energía.

El proyecto incluye un **Dockerfile**, por lo que puede ejecutarse fácilmente en contenedores sin necesidad de instalar dependencias adicionales en el sistema host.

---

## Cómo usar

1. Descargar el Dockerfile y construir el contenedor 

docker build -t dashboard-ups .

Ejecutar el contenedor:

Nota: Esta version usa:
    extra_hosts:
    - "host.docker.internal:host-gateway"
Para poder interactuar con localhost y hacerle las consultas del estado a upsc.

Si se quiere probar en localhost, hay que exponer el puerto 18000 (-p 18000:18000).

Acceder desde el navegador:

http://localhost:18000/ups 

El dashboard se actualizará automáticamente cada 2 segundos mostrando los datos del SAI.

Si se quiere ver directamente la informacion recibida por upsc se puede consultar usando /ups/raw en la url.

Configuración del SAI

Para configurar el sistema se puede tomar esta guía de ejemplo: 
[Administración básica del SAI Salicru SPS One 900VA con NUT]
(https://www.jormc.es/tutoriales/administracion-basica-del-sai-salicru-spsone-900va-con-nut/#Introduccion)

La única diferencia recomendada es cambiar la parte de:

LISTEN 127.0.0.1 3493

por

LISTEN 0.0.0.0 3493

para permitir que NUT escuche en todas las interfaces y pueda ser accedido por la API.
