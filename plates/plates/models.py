from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class NumberPlate(models.Model):
    number = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='number_plate')

    def save(self, *args, **kwargs):
        self.number = self.number.upper()
        return super(NumberPlate, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.number)
