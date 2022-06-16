from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Deletes users'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            try:
                user_to_delete = User.objects.get(pk=user.id)
                if not user_to_delete.is_superuser:
                    user_to_delete.delete()
            except User.DoesNotExist:
                pass
        self.stdout.write(self.style.SUCCESS('Successfully deleted users'))
