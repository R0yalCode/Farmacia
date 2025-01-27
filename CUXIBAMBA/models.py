from django.db import models

# Clase Abstracta Persona
class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    class Meta:
        abstract = True

# Clase Cliente (hereda de Persona)
class Cliente(Persona):
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

# Clase Usuario (hereda de Persona)
class Usuario(Persona):
    clave = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

# Clase Rol
class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Clase Permisos
class Permisos(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='permisos')
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE, related_name='permisos')
    puede_crear = models.BooleanField(default=False)
    puede_editar = models.BooleanField(default=False)
    puede_eliminar = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.rol} - {self.menu}"

# Clase Menu
class Menu(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Clase Provincia
class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

# Clase Canton
class Canton(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='cantones')
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

# Clase Parroquia
class Parroquia(models.Model):
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE, related_name='parroquias')
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

# Clase Farmacia
class Farmacia(models.Model):
    codigo_farmacia = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    grupo = models.CharField(max_length=50)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='farmacias')

    def __str__(self):
        return self.nombre

# Clase Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

# Clase Direccion
class Direccion(models.Model):
    farmacia = models.OneToOneField(Farmacia, on_delete=models.CASCADE, related_name='direccion')
    calle_principal = models.CharField(max_length=100)
    calle_secundaria = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f"{self.calle_principal} y {self.calle_secundaria}"

# Clase Horario
class Horario(models.Model):
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE, related_name='horarios')
    descripcion = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return self.descripcion

# Clase Pedido
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    farmacia_origen = models.ForeignKey(Farmacia, on_delete=models.CASCADE, related_name='pedidos_origen')
    fecha = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"

# Clase Entrega
class Entrega(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='entregas')
    direccion = models.TextField()
    fecha_entrega = models.DateTimeField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Entrega {self.id} - {self.estado}"

# Clase Venta
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ventas')
    cantidad = models.IntegerField()
    farmacia_origen = models.ForeignKey(Farmacia, on_delete=models.CASCADE, related_name='ventas_origen')
    farmacia_destino = models.ForeignKey(Farmacia, on_delete=models.CASCADE, related_name='ventas_destino', null=True, blank=True)
    metodo_entrega = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta {self.id}"

# Clase Transaccion
class Transaccion(models.Model):
    tipo_transaccion = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()
    monto_total = models.FloatField()
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE, related_name='transacciones')

    def __str__(self):
        return f"Transacción {self.id}"