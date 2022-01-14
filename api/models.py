from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Car(models.Model):
    make = models.CharField(max_length = 200)
    model = models.CharField(max_length = 13)

    class Meta:
        unique_together =('make', 'model')

    def __str__(self):
        return f'{self.make} {self.model}'

class Rating(models.Model):
    rating = models.IntegerField(validators = [
            MaxValueValidator(5),
            MinValueValidator(1)
            ])
    car_id = models.ForeignKey(Car, related_name = 'ratings', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.car_id.make[0]}_{self.car_id.model} {"*" * self.rating}'