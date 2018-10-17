# IPContainer

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Build Status](https://travis-ci.com/harvestcore/IPContainer.svg?branch=master)](https://travis-ci.com/harvestcore/IPContainer)



## ¿Qué es?

IPContainer es un microservicio centrado en el almacenamiento y gestión básica de direcciones IP. Permite tener almacenadas una serie de direcciones IP en un mismo lugar, agrupadas por tipo de red:

- **PAN** (Personal Area Network)
- **LAN** (Local Area Network)
- **WAN** (Wide Area Network)
- **SAN** (Storage Area Network)
- **VLAN** (Virtual Local Area Network)
- **WLAN** (Wireles Local Area Network)

Por otro lado permite almacenar direcciones IP de servidores DNS.



## ¿Por qué?

La idea surge tras necesitar un lugar donde tener una serie de direcciones IP organizadas y almacenadas en un mismo lugar, sin depender de mirar archivos de configuración o uso de otras aplicaciones.



Más info:

- [Web del proyecto](https://harvestcore.github.io/es/ipcontainer/index.html).
- [Web del repositorio](https://harvestcore.github.io/IPContainer).
- [Funcionalidades](doc/funcionalidades.md).
- [Base de datos](doc/bd.md).



## Herramientas y servicios

- [**Python**](https://www.python.org/): Lenguaje principal de programación.
  - [**Flask**](http://flask.pocoo.org/): Framework principal.
  - [**SQLAlchemy**](https://www.sqlalchemy.org/): Como [ORM](https://es.wikipedia.org/wiki/Mapeo_objeto-relacional).
- [**MariaDB**](https://mariadb.org/): Gestor de base de datos.
- [**Travis-CI**](https://travis-ci.org/): Para integración contínua.



## Pasos a seguir en el desarrollo de IPContainer

- [x] Descripción general.
- [x] Elección de herramientas para su desarrollo.
- [ ] Integración continua. Tests.
- [ ] Despliegue del microservicio en un PaaS.
- [ ] Despliegue en docker.
- [ ] Despliegue automático a las plataformas de producción.
