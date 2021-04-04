from django.db import models
from phone_field import PhoneField
import birthday

class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name


class FederalDistrict(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    federal_district_name = models.CharField(max_length=50)

    def __str__(self):
        return self.federal_district_name


class Region(models.Model):
    federal_district = models.ForeignKey(FederalDistrict, on_delete=models.CASCADE)
    region_number = models.CharField(max_length=2)
    abc_name = models.CharField(max_length=50)
    region_name = models.CharField(max_length=50)

    def __str__(self):
        return self.region_name


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class Position(models.Model):
    position_name = models.CharField(max_length=50)

    def __str__(self):
        return self.position_name


class Palate(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    palate_name = models.CharField(max_length=50)
    email1 = models.EmailField(max_length=254)
    email2 = models.EmailField(max_length=254)
    email3 = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    website = models.URLField(max_length=200)
    tax_no = models.CharField(max_length=15)
    kpp_no = models.CharField(max_length=10)
    bank_name = models.CharField(max_length=50)
    bank_account = models.CharField(max_length=30)
    bank_corrno = models.CharField(max_length=30)
    bank_bicno = models.CharField(max_length=10)

    def __str__(self):
        return self.palate_name


class Person(models.Model):
    palate = models.ForeignKey(Palate, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=50)
    address_name = models.CharField(max_length=50)
    birthday = models.DateField()
    personal_data_date = models.DateField()
    email1 = models.EmailField(max_length=254)
    email2 = models.EmailField(max_length=254)
    email3 = models.EmailField(max_length=254)
    registered_address = models.CharField(max_length=50)
    post_address = models.CharField(max_length=50)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    mobile_phone = PhoneField(blank=True, help_text='Mobile phone number')
    tax_no = models.CharField(max_length=15)
    active = models.BooleanField()
    male_gender = models.BooleanField()
    education_document_series = models.CharField(max_length=10)
    education_document_number = models.CharField(max_length=10)
    education_document_surname = models.CharField(max_length=20)

    def __str__(self):
        return self.person_name


class EventType(models.Model):
    event_type_name = models.CharField(max_length=50)
    event_type_comment = models.CharField(max_length=100)

    def __str__(self):
        return self.event_type_name


class Manager(models.Model):
    manager_name = models.CharField(max_length=50)
    manager_login = models.CharField(max_length=20)
    write_access = models.BooleanField()
    administrator = models.BooleanField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.manager_name


class Event(models.Model):
    eventtype = models.ForeignKey(EventType, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    palate = models.ForeignKey(Palate, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    place = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50)
    event_conditions = models.CharField(max_length=50)
    event_comment = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    request_deadline = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_hours = models.IntegerField()
    regular = models.BooleanField()
    event_folder = models.FileField(upload_to=None, max_length=254)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)