from django.db import models


class BIO(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth = models.DateField(verbose_name='You first see this world in')
    biography = models.TextField()
    phone = models.CharField(max_length=12)
    skype = models.CharField(max_length=25)
    other = models.CharField(max_length=255)

    class Meta:
        db_table = 'bio'