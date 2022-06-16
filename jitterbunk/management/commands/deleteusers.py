from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

usernames = ['justin', 'genna', 'derek', 'jade', 'saul', 'earl', 'seymour', 'tony', 'arthur', 'markus', 'olivia', 'joline', 'maximum', 'britt', 'haywood', 'dylan', 'rodrick', 'roberta', 'lulu', 'billie', 'hugh', 'maryann', 'tanisha', 'clark', 'leda', 'kylie', 'lucius', 'darwin', 'irene', 'lilla', 'numbers', 'antonio', 'herma', 'charlyn', 'aaron', 'elijah', 'carey', 'michelle', 'dori', 'elizabeth', 'jessica', 'josie', 'shelly', 'bernard', 'tyson', 'stan', 'willy', 'amanda', 'elbert', 'gene', 'brandon', 'connie', 'nicholas', 'martin']

class Command(BaseCommand):
    help = 'Deletes users'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for name in usernames:
                if User.objects.filter(username=name).exists():
                    user = User.objects.get(username=name)
                    user.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted users'))
