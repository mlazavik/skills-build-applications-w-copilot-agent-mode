from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='superman@dc.com', name='Superman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Activities
        Activity.objects.bulk_create([
            Activity(user='Iron Man', activity_type='Running', duration=30, date='2026-03-01'),
            Activity(user='Captain America', activity_type='Cycling', duration=45, date='2026-03-02'),
            Activity(user='Spider-Man', activity_type='Jumping', duration=20, date='2026-03-03'),
            Activity(user='Batman', activity_type='Martial Arts', duration=60, date='2026-03-01'),
            Activity(user='Superman', activity_type='Flying', duration=120, date='2026-03-02'),
            Activity(user='Wonder Woman', activity_type='Lifting', duration=50, date='2026-03-03'),
        ])

        # Leaderboard
        Leaderboard.objects.bulk_create([
            Leaderboard(team='Marvel', points=95),
            Leaderboard(team='DC', points=90),
        ])

        # Workouts
        Workout.objects.bulk_create([
            Workout(name='Hero Endurance', description='Endurance workout for heroes', suggested_for='Marvel'),
            Workout(name='Power Training', description='Strength workout for DC heroes', suggested_for='DC'),
        ])

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
