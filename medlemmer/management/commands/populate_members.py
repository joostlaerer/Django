from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from medlemmer.models import Member


class Command(BaseCommand):
    help = 'Populate database with test members'

    def handle(self, *args, **options):
        # Sample member data
        members_data = [
            {
                'username': 'john_doe',
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john@example.com',
                'phone': '+1-555-0101',
                'address': '123 Main St',
                'city': 'New York',
                'country': 'USA',
                'bio': 'Software developer and tech enthusiast.'
            },
            {
                'username': 'jane_smith',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'email': 'jane@example.com',
                'phone': '+1-555-0102',
                'address': '456 Oak Ave',
                'city': 'Los Angeles',
                'country': 'USA',
                'bio': 'Designer and creative thinker.'
            },
            {
                'username': 'mike_johnson',
                'first_name': 'Mike',
                'last_name': 'Johnson',
                'email': 'mike@example.com',
                'phone': '+1-555-0103',
                'address': '789 Pine Rd',
                'city': 'Chicago',
                'country': 'USA',
                'bio': 'Project manager and team leader.'
            },
            {
                'username': 'emma_wilson',
                'first_name': 'Emma',
                'last_name': 'Wilson',
                'email': 'emma@example.com',
                'phone': '+1-555-0104',
                'address': '321 Elm St',
                'city': 'Boston',
                'country': 'USA',
                'bio': 'Data analyst and research specialist.'
            },
            {
                'username': 'alex_brown',
                'first_name': 'Alex',
                'last_name': 'Brown',
                'email': 'alex@example.com',
                'phone': '+1-555-0105',
                'address': '654 Maple Dr',
                'city': 'Seattle',
                'country': 'USA',
                'bio': 'Full-stack developer and open source contributor.'
            },
        ]

        created_count = 0
        for member_data in members_data:
            username = member_data.pop('username')
            email = member_data.pop('email')

            # Create or get the user
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'first_name': member_data.pop('first_name', ''),
                    'last_name': member_data.pop('last_name', ''),
                }
            )

            # Update or create the member profile
            member, member_created = Member.objects.update_or_create(
                user=user,
                defaults=member_data
            )

            if member_created or created:
                self.stdout.write(self.style.SUCCESS(f'Created member: {username}'))
                created_count += 1
            else:
                self.stdout.write(self.style.WARNING(f'Updated member: {username}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created/updated {created_count} members!'))
