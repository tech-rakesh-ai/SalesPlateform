import requests
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from accounts.models import CustomUser, Address


class Command(BaseCommand):
    help = 'Create 50 custom user accounts with dummy data'

    def handle(self, *args, **options):
        try:
            response = requests.get('https://dummyjson.com/users')
            response.raise_for_status()
            user_data = response.json()["users"][:50]
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching user data: {e}'))
            return
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f'Error parsing JSON: {e}'))
            self.stdout.write(self.style.ERROR(f'Response content: {response.text}'))
            return

        for data in user_data:
            address = Address.objects.create(address=data.get('address', ''))
            email = CustomUser.objects.get(email=data.get('email', '')).exists()
            if email != None:
                custom_user = CustomUser.objects.create(
                    username=get_random_string(10),
                    first_name=data.get('firstName', ''),
                    last_name=data.get('lastName', ''),
                    middle_name=data.get('middleName', ''),
                    age=data.get('age'),
                    gender=data.get('gender', ''),
                    email=data.get('email', ''),
                    phone=data.get('phone', ''),
                    birth_date=data.get('birthDate'),
                    address=address,

                )

                self.stdout.write(self.style.SUCCESS(f'Successfully created custom user: {custom_user}'))

            # def check_exist_email():
            #     email = CustomUser.objects.get().
