from django.db import models


class Person(models.Model):
    ARTIST = 'ART'
    CUSTOMER = 'CUS'
    ACCOUNT_TYPE = [
        (ARTIST, 'Artist'),
        (CUSTOMER, 'Customer'),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=20)
    post_code_1 = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    account_type = models.CharField(
        max_length=3,
        choices=ACCOUNT_TYPE,
    )
    profile_image = models.ImageField(null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class Artist(Person):
    def __str__(self):
        return self.first_name
