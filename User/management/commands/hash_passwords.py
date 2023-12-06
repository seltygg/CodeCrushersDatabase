# your_app/management/commands/hash_passwords.py

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from ...models import Accounts

class Command(BaseCommand):
    help = 'Hashes all passwords currently present in the database'

    def handle(self, *args, **options):
        accounts = Accounts.objects.all()

        for account in accounts:
            # Check if the password is not already hashed
            if not account.accountpassword.startswith(('pbkdf2_sha256$', 'bcrypt', 'argon2')):
                # Hash the password using make_password
                hashed_password = make_password(account.accountpassword)

                # Update the account password with the hashed password
                account.accountpassword = hashed_password

                # Save the updated account
                account.save()

        self.stdout.write(self.style.SUCCESS('Successfully hashed all passwords'))
