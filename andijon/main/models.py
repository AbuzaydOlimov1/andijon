from django.db import models


class photo(models.Model):
    photo = models.ImageField()


class Banner(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.title


class ObjectsNear(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    iconcode = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class AboutBroker(models.Model):
    iconcode = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Broker(models.Model):
    name = models.CharField(max_length=255)
    rate = models.FloatField()
    reviews = models.IntegerField()
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Step(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Interier(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Builder(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField()
    photo = models.ImageField()
    news = models.IntegerField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    delivery_time = models.DateField()
    area = models.IntegerField()
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    installment = models.CharField(max_length=255)
    floors = models.IntegerField()
    amount = models.IntegerField()
    heigt = models.IntegerField()
    material = models.CharField(max_length=255)
    parking = models.CharField(max_length=255)
    interier = models.ForeignKey(Interier, on_delete=models.CASCADE)
    rooms = models.IntegerField()
    photo = models.ManyToManyField('photo')
    price = models.IntegerField()
    quality = models.ForeignKey(Category, on_delete=models.CASCADE)
    balcony = models.CharField(max_length=255)
    on_proccess = models.BooleanField(default=True)
    liked = models.BooleanField(default=False)
    heating_system = models.CharField(max_length=255)
    security = models.BooleanField(default=False)
    location = models.TextField()
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    objects_near = models.ForeignKey(ObjectsNear, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PaymentOption(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.title


class SpecialOffer(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    photo = models.ImageField()
    discount = models.IntegerField()

    def __str__(self):
        return self.title


class Bid(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Link(models.Model):
    tg = models.CharField(max_length=255)
    insta = models.CharField(max_length=255)
    yt = models.CharField(max_length=255)
    fb = models.CharField(max_length=255)

