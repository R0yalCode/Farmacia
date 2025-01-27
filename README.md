# CUXIBAMBA ROYAL
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
- *Frontend:* Interfaz de Administración de Django para la gestión y html buscado en la web.

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
![Image](https://github.com/user-attachments/assets/14dd6280-dfa0-40b7-ba02-c2f6a7db1b52)
>Clase principal Farmacia

![Image](https://github.com/user-attachments/assets/4a48d1ae-34eb-471a-aae7-4b7bbea5347b)
>usuario

![Image](https://github.com/user-attachments/assets/7c1287cc-6c1b-418c-a843-598590759a40)
>Ubicacion-zona

![Image](https://github.com/user-attachments/assets/74d44bf9-81d6-4bdf-be94-1045d4af1a4d)
>Pedidos

![Image](https://github.com/user-attachments/assets/df12d2fd-fcc1-4b6c-be74-c97ec6b08169)
>Venta-Iventario-Pedidos

![Image](https://github.com/user-attachments/assets/3d6ed571-8c2c-4c04-bda7-fc5062ca6b32)
>Telefono-Horario-Turno

---
### Interfas de usuario
![Image](https://github.com/user-attachments/assets/884cd89f-23b8-48a6-9380-c0c4c5e3b9e0)
>Home

![Image](https://github.com/user-attachments/assets/6a770abf-a44e-4bdd-8b1e-aca721802631)
>Cita

![Image](https://github.com/user-attachments/assets/d5246fa5-46f3-4c08-a63a-93040f1aad4d)
>Galeria

![Image](https://github.com/user-attachments/assets/30538ceb-170c-4b8c-89e2-d3ecb81496f5)
>Blog

![Image](https://github.com/user-attachments/assets/684a31ef-b790-4331-9b1f-e407fc5fea7b)
>Contactame
---

## Instalación y Configuración

### Requisitos previos

- Python 3.13 o superior.
- pip para instalar dependencias.
- Virtualenv (opcional, pero recomendado).

### Pasos de Instalación

1. *Clonar el repositorio:*
   ```bash
   git clone https://github.com/R0yalCode/Farmacia.git
   cd farmacia-system
