from django.core.management.base import BaseCommand
from courses.models import Facility

FACILITIES = [
    {
        'name': 'Transportation',
        'slug': 'transportation',
        'description': 'Experience convenience and safety with our cozy and comfortable doorstep transportation service for our students. Our fleet of mini-buses, each with a capacity of sixteen school children, ensures a secure and enjoyable commute to and from school.',
    },
    {
        'name': 'Library',
        'slug': 'library',
        'description': 'Our well-stocked library offers a wide range of books and resources to foster a love for reading and support academic growth.',
    },
    {
        'name': 'Dance',
        'slug': 'dance',
        'description': 'We provide dance classes and activities to encourage creativity, rhythm, and physical fitness among our students.',
    },
    {
        'name': 'Computer Lab',
        'slug': 'computer-lab',
        'description': 'Our modern computer lab is equipped with the latest technology to enhance digital literacy and learning.',
    },
    {
        'name': 'Scout',
        'slug': 'scout',
        'description': 'Scouting activities help students develop leadership, teamwork, and life skills in a fun and engaging environment.',
    },
    {
        'name': 'Sports',
        'slug': 'sports',
        'description': 'We offer a variety of sports programs to promote physical health, teamwork, and sportsmanship.',
    },
    {
        'name': 'Yoga',
        'slug': 'yoga',
        'description': 'Yoga sessions help students improve flexibility, concentration, and overall well-being.',
    },
    {
        'name': 'AC Room',
        'slug': 'ac-room',
        'description': 'Our air-conditioned classrooms provide a comfortable learning environment throughout the year.',
    },
]

class Command(BaseCommand):
    help = 'Create default Facility objects for the main school services.'

    def handle(self, *args, **options):
        created = 0
        for idx, fac in enumerate(FACILITIES):
            obj, was_created = Facility.objects.get_or_create(
                slug=fac['slug'],
                defaults={
                    'name': fac['name'],
                    'description': fac['description'],
                    'order': idx,
                    'is_active': True,
                }
            )
            if was_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {obj.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {obj.name}"))
        self.stdout.write(self.style.SUCCESS(f"Total facilities processed: {len(FACILITIES)}. Newly created: {created}")) 