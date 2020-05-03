from django.db import models

# Create your models here.
class BaseItem(models.Model):
	january = models.BooleanField(default=False)
	february = models.BooleanField(default=False)
	march = models.BooleanField(default=False)
	april = models.BooleanField(default=False)
	may = models.BooleanField(default=False)
	june = models.BooleanField(default=False)
	july = models.BooleanField(default=False)
	august = models.BooleanField(default=False)
	september = models.BooleanField(default=False)
	october = models.BooleanField(default=False)
	november = models.BooleanField(default=False)
	december = models.BooleanField(default=False)

	start_time = models.TimeField(blank=True, null=True)
	end_time = models.TimeField(blank=True, null=True)

	class Meta:
		abstract = True


class Fish(BaseItem):
	location_choices = (
		("sea", "Sea"),
		("river", "River"),
		("pier", "Pier"),
		("pond", "Pond"),
		("river-clifftop", "River (Clifftop)"),
	)
	name = models.CharField(max_length=128, unique=True)
	price = models.IntegerField(default=0)
	location = models.CharField(max_length=64, choices=location_choices)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ("name",)


class Bug(BaseItem):
	name = models.CharField(max_length=128)
	price = models.IntegerField()

	class Meta:
		ordering = ("name",)
