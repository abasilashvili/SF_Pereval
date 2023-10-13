from django.db import models

STATUS = [
    ('new', 'Новая заявка'),
    ('pending', 'Модератор взял в работу'),
    ('accepted', 'Модерация прошла успешно'),
    ('rejected', 'Модерация прошла, информация не принята'),
]

LEVEL = [
    ('1A', '1A'),
    ('1B', '1B'),
    ('1C', '1C'),
]


class Coord(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()


class Level(models.Model):
    winter = models.CharField(max_length=2, choices=LEVEL, null=True, blank=True)
    summer = models.CharField(max_length=2, choices=LEVEL, null=True, blank=True)
    autumn = models.CharField(max_length=2, choices=LEVEL, null=True, blank=True)
    spring = models.CharField(max_length=2, choices=LEVEL, null=True, blank=True)


class PerevalImages(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20)

    class Meta:
        db_table = 'pereval_images'


class PerevalUser(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.email}'


class PerevalAdded(models.Model):
    date_added = models.DateField(auto_now_add=True)
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    other_title = models.CharField(max_length=255)
    connect = models.TextField(blank=True, default='')
    add_time = models.TimeField(auto_now_add=True)
    user_id = models.ForeignKey(PerevalUser, related_name='perevals', on_delete=models.CASCADE)
    coord_id = models.ForeignKey(Coord, related_name='coords', on_delete=models.CASCADE)
    level_id = models.ForeignKey(Level, related_name='levels', on_delete=models.CASCADE)
    image_id = models.ForeignKey(PerevalImages, related_name='images', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='new')

    class Meta:
        db_table = 'pereval_added'

    def __str__(self):
        return f'{self.title}'


class PerevalAreas(models.Model):
    id_parent = models.IntegerField(null=True)
    title = models.TextField(null=True)

    class Meta:
        db_table = 'pereval_areas'


class SprActivitiesTypes(models.Model):
    title = models.TextField(null=True)

    class Meta:
        db_table = 'spr_activities_types'