from django.db import models


class BIO(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth = models.DateField(verbose_name='You first see this world in')
    biography = models.TextField(blank=True)
    phone = models.CharField(max_length=12, blank=True)
    skype = models.CharField(max_length=25, blank=True)
    other = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'bio'