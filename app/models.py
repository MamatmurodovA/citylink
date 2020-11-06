from django.db import models


class Survey(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=25, choices=GENDERS)
    room_number = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    review = models.TextField()


class Service(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ServiceRank(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='ranks')
    rank = models.PositiveIntegerField()
