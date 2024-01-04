from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=255) #El form debe usar widget=forms.PasswordInput

    # Override a print de objeto, de esta forma obtenemos un print legible
    def __str__(self):
        return self.name
    
class Resena(models.Model):
    id_user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category=models.CharField(max_length=30)
    product=models.CharField(max_length=30) # ej "Taladro Bauker"
    purchase_place=models.CharField(max_length=30, blank=True, null=True) # ej "Homecenter". Nullable, desde form puede recibir blank
    used_time=models.CharField(max_length=10, blank=True, null=True)  #ej: "2 dias". Nullable, desde form puede recibir blank
    status=models.BinaryField()   # 1 si esta usado, 0 si esta nuevo
    product_valoration=models.IntegerField()
    resena_valoration=models.IntegerField()
    Image=models.ImageField()
    description=models.CharField(max_length=255)
    

class Comentario(models.Model):
    id_resena = models.ForeignKey(Resena, on_delete=models.DO_NOTHING) # Relacion con Resenas, on delete no afecta a la resena
    id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length = 255)

    def __str__(self):
        return self.description





