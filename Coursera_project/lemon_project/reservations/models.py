from django.db import models

# Create your models here.
class Reservations(models.Model):
    name = models.CharField(max_length=50)
    guests = models.IntegerField()
    date = models.DateField()
    # table = forms.IntegerField()
    # celebration = (('1','anniversary'), ('2','birthday'), ('3','other'))
    # ocassion = forms.ChoiceField(choices=celebration)
    # email = forms.EmailField()

    def __str__(self):
        return str(self.date) + "  " + str(self.guests)

class MenuCategory(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    category_id = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,
        )
