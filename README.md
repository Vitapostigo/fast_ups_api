Es necesario darle network host para que pueda acceder al puerto que expone el SAI en el PC.

Para configurar el sistema se puede tomar esta guia de ejemplo:
https://www.jormc.es/tutoriales/administracion-basica-del-sai-salicru-spsone-900va-con-nut/#Introduccion
La unica diferencia es que para permitir que escuche en otras ips se recomienda cambiar la parte de:
LISTEN 127.0.0.1 3493 por LISTEN 0.0.0.0 3493
