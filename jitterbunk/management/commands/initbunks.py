from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from jitterbunk.models import Bunk
from random import sample
from django.utils import timezone

class Command(BaseCommand):
    help = 'Deletes users'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        users = list(User.objects.all())
        if len(users) < 2:
            return
        for i in range(20):
            user1, user2 = sample(users, 2)
            bunk = Bunk(from_user=user1, to_user=user2, time=timezone.now())
            bunk.save()
        self.stdout.write(self.style.SUCCESS('Successfully sent bunks'))
