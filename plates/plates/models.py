from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class NumberPlate(models.Model):
    # There are a lot of different formats of plate numbers, see:
    # https://regitra.lt/lt/paslaugos-ir-veikla/numerio-zenklai/numerio-zenklu-tipai
    number = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='number_plate')

    def __str__(self):
        return '%s' % (self.number)
