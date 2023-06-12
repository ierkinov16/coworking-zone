from django.db import models


class Room(models.Model):
    class RoomType(models.TextChoices):
        focus = 'focus', 'Focus'
        team = 'team', 'Team'
        conference = 'conference', 'Conference',

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=RoomType.choices, default=RoomType.team)
    capacity = models.SmallIntegerField()

    def __str__(self):
        return self.name

