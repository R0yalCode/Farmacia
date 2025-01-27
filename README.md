# Sistema de Gestión para una Cadena de Farmacias

## Descripción del Problema

Este proyecto tiene como objetivo desarrollar un sistema de gestión para una cadena de farmacias con múltiples sucursales. La solución debe permitir la gestión de inventarios, ventas, transferencias entre sucursales y seguimiento de pedidos, con énfasis en garantizar la disponibilidad de medicamentos para los clientes.

### Características principales del sistema:
1. *Venta de Medicamentos:*
   - Permitir la venta de productos disponibles en la sucursal seleccionada.
   - Si el producto no está disponible en la sucursal, habilitar la venta desde otra sucursal.
   - Ofrecer opciones de entrega: retiro en la sucursal de origen o entrega en la sucursal de compra.

2. *Gestión de Inventarios:*
   - Controlar el stock de medicamentos en cada sucursal.
   - Facilitar la actualización del inventario en tiempo real.

3. *Transferencias entre Sucursales:*
   - Permitir la compra de medicamentos desde una sucursal diferente.
   - Registrar el tránsito y llegada de productos entre sucursales.

4. *Registro de Clientes y Pedidos:*
   - Gestionar clientes, pedidos y el seguimiento de entregas.

5. *Autenticación y Roles de Usuario:*
   - Crear roles diferenciados para administrador, empleado de sucursal y cliente.
   - Gestionar accesos y permisos para garantizar la seguridad del sistema.

---

## Tecnologías Utilizadas

El sistema ha sido desarrollado utilizando las siguientes herramientas y tecnologías:

- *Framework:* Django (Python).
- *Base de Datos:* SQLite (por defecto de Django) con la posibilidad de migrar a PostgreSQL.
- *Frontend:* Interfaz de Administración de Django para la gestión.
- *Despliegue:* Preparado para ser desplegado en servidores como Heroku o cualquier servicio compatible con WSGI.

---

## Estructura del Proyecto

### Modelos Principales

1. *Farmacia:* Representa cada sucursal de la cadena de farmacias con información de ubicación y horarios.
2. *Producto:* Almacena la información de los medicamentos disponibles.
3. *Cliente:* Representa a los usuarios que realizan pedidos.
4. *Usuario:* Gestiona los roles y accesos de los empleados y administradores.
5. *Venta:* Registra cada transacción de compra de un cliente.
6. *Pedido y Entrega:* Gestiona los pedidos realizados y las entregas asociadas.
7. *Transacción:* Registra los movimientos financieros y operativos del sistema.

### Relaciones entre Clases

- *Farmacia:* Relacionada con productos, pedidos, entregas y horarios.
- *Usuario y Roles:* La clase Usuario gestiona permisos a través de roles y menús.
- *Pedidos y Entregas:* Un pedido puede tener múltiples entregas asociadas.

### Diagramas UML
Se ha trabajado en diagramas para describir las relaciones entre las clases y su implementación en Django. Consulte la documentación del repositorio para detalles sobre los diagramas.

---

## Instalación y Configuración

### Requisitos previos

- Python 3.8 o superior.
- pip para instalar dependencias.
- Virtualenv (opcional, pero recomendado).

### Pasos de Instalación

1. *Clonar el repositorio:*
   ```bash
   git clone https://github.com/tu_usuario/farmacia-system.git
   cd farmacia-system
