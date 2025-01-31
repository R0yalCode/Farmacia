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
![Image](https://github.com/user-attachments/assets/c8b53e90-40b6-45d9-96a6-1be0d3ab4d3a)
>Clase principal Farmacia

![Image](https://github.com/user-attachments/assets/b88b1417-e06c-4092-bccc-77fcaf1d6b77)
>usuario

![Image](https://github.com/user-attachments/assets/55ecb5aa-08ce-4823-8b29-bc6deaf5f671)
>Ubicacion-zona

![Image](https://github.com/user-attachments/assets/4b551a90-034e-4d69-b770-3a7c55bbc2b3)
>Pedidos

![Image](https://github.com/user-attachments/assets/470985d7-57a1-4b93-8e3b-f2a7cbf3f492)
>Venta-Iventario-Pedidos

![Image](https://github.com/user-attachments/assets/261e84e6-2ae7-4e48-8bfb-376b6bfe4f7d)
>Telefono-Horario-Turno

---
### Interfas de usuario
![Image](https://github.com/user-attachments/assets/c104408a-656a-4904-99ba-e8b565bc1f05)
>Home

![Image](https://github.com/user-attachments/assets/6a770abf-a44e-4bdd-8b1e-aca721802631)
>Cita

![Image](https://github.com/user-attachments/assets/d5246fa5-46f3-4c08-a63a-93040f1aad4d)
>Galeria

![Image](https://github.com/user-attachments/assets/30538ceb-170c-4b8c-89e2-d3ecb81496f5)
>Blog

![Image](https://github.com/user-attachments/assets/684a31ef-b790-4331-9b1f-e407fc5fea7b)
>Contactame

![image](https://github.com/user-attachments/assets/78a30bb7-065f-447f-a122-9ac95d8c45ac)
>Resitrarse

### CUXIBAMBA-ADMIN
![Image](https://github.com/user-attachments/assets/be1374bf-01d5-4f8e-8329-254dd01d5ad1)
>Admin

### Registro
![image](https://github.com/user-attachments/assets/f6b561dc-8e01-4db3-96e4-cbbf1ece33e1)
>Registro de clientes

### Creacion de cuenta
![Image](https://github.com/user-attachments/assets/571edb84-87c0-415b-99fa-f0e294acc7b7)
>Creacion de una nueva cuenta

### ADMIN-DJANGO
![image](https://github.com/user-attachments/assets/2a174576-570f-4bd1-8e38-4f1ac3704703)
>admin

![image](https://github.com/user-attachments/assets/b045cc6d-dda6-4a35-adaa-3d8286adb1a4)
>Pedidos

![image](https://github.com/user-attachments/assets/d9782cee-af6b-467e-8256-5adf574ab661)
>Productos

![image](https://github.com/user-attachments/assets/c0d9d04d-5c66-4e92-9a37-3dd30ce4fec8)
>Transaccion

![image](https://github.com/user-attachments/assets/18037589-e147-47ab-9fd4-597ed4e84f59)
>venta
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
