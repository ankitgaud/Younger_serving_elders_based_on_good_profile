from django.db import models

# Create your models here.

class Young_user(models.Model):
	Y_username = models.CharField(primary_key=True,max_length=20)
	name = models.CharField('Name', max_length=120)
	address = models.TextField(blank=True)
	gender = models.CharField(max_length=20)
	dob = models.DateField()
	social_profile = models.CharField('Social link', max_length=220)
	average_rating = models.IntegerField()
	experience = models.IntegerField()
	age = models.IntegerField()

	def __str__(self):
		return self.name


class elder_table(models.Model):
	younger_user = models.CharField(max_length=20)
	rating_by_elder = models.IntegerField()
	review_by_elder = models.CharField('Review', max_length=220)
	time_duration = models.IntegerField() 
	elder_user = models.CharField(max_length=20)

	def __str__(self):
		return self.elder_user

class younger_table(models.Model):
	elder_user = models.CharField(max_length=20)
	rating_by_younger = models.IntegerField()
	review_by_younger = models.CharField('Review', max_length=220)
	start_date = models.DateField(null=True)
	younger_user = models.CharField(max_length=20)

	def __str__(self):
		return self.elder_user



class ELDER_user(models.Model):
	E_username = models.CharField(primary_key=True,max_length=20)
	name1 = models.CharField('Name', max_length=120)
	address1 = models.TextField(blank=True)
	gender1 = models.CharField(max_length=20)
	dob1 = models.DateField()
	average_rating1 = models.IntegerField()

	def __str__(self):
		return self.name1


class Current_status_younger(models.Model):
	username = models.CharField(primary_key=True,max_length=20)
	elder_1 = models.CharField(max_length=20, blank=True)
	elder_2 = models.CharField(max_length=20, blank=True)
	elder_3 = models.CharField(max_length=20, blank=True)
	elder_4 = models.CharField(max_length=20, blank=True)
	elder_6 = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.username


