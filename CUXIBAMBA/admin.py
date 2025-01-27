from django.contrib import admin
from .models import Cliente, Usuario, Rol, Permisos, Menu, Provincia, Canton, Parroquia, Farmacia, Producto, Direccion, Horario, Pedido, Entrega, Venta, Transaccion

admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Permisos)
admin.site.register(Menu)
admin.site.register(Provincia)
admin.site.register(Canton)
admin.site.register(Parroquia)
admin.site.register(Farmacia)
admin.site.register(Producto)
admin.site.register(Direccion)
admin.site.register(Horario)
admin.site.register(Pedido)
admin.site.register(Entrega)
admin.site.register(Venta)
admin.site.register(Transaccion)