from django.db import models
from django.contrib.auth.models import AbstractUser


class TelegramUser(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    chat_id = models.CharField(max_length=255, unique=True)
    # username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username or f'Telegram ID: {self.chat_id}'
    
    # def save(self, force_insert=False, force_update=False):
    #     is_new = self.id is None
    #     super(ModelA, self).save(force_insert, force_update)
    #     if is_new:
    #         ModelB.objects.create(thing=self)
