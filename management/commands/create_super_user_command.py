# Import necessary modules
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


# Define your custom management command
class Command(BaseCommand):
    help = 'Creates a superuser with admin access'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'admin'
        email = 'prash98400@gmail.com'
        password = get_random_string(length=12)  # Generate a random password of length 12

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(username, email, password)
            user.user_type = '1'  # Set user_type as admin
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created with password: {password}'))
        else:
            user = User.objects.get(username=username)
            if not user.is_superuser:
                user.is_superuser = True
                user.user_type = '1'  # Set user_type as admin
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" updated to admin role'))
            else:
                self.stdout.write(self.style.NOTICE(f'Superuser "{username}" already exists'))
