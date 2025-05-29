from django.db import models



class VrstaJela(models.Model):
    naziv = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.naziv
    

class Jelo(models.Model):
    vrsta = models.ForeignKey(VrstaJela, on_delete=models.CASCADE, related_name='jela')
    naziv = models.CharField(max_length=100, unique=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    opis = models.TextField(blank=True, null=True)
    slika = models.ImageField(upload_to='jela/', blank=True, null=True)

    def __str__(self):
        return self.naziv
