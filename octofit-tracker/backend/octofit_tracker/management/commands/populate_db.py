from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data (delete individually for Djongo compatibility)
        for model in [Leaderboard, Activity, User, Team, Workout]:
            for obj in model.objects.all():
                obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', username='IronMan', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', username='Batman', team=dc)
        clark = User.objects.create(email='clark@kent.com', username='Superman', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='Strength')
        running = Workout.objects.create(name='Running', description='Cardio workout', suggested_for='Endurance')

        # Create Activities
        Activity.objects.create(user=tony, activity_type='Pushups', duration=30, calories_burned=200, date=date(2023, 1, 1))
        Activity.objects.create(user=steve, activity_type='Running', duration=45, calories_burned=400, date=date(2023, 1, 2))
        Activity.objects.create(user=bruce, activity_type='Pushups', duration=20, calories_burned=150, date=date(2023, 1, 3))
        Activity.objects.create(user=clark, activity_type='Running', duration=60, calories_burned=500, date=date(2023, 1, 4))

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=120, rank=2)
        Leaderboard.objects.create(user=steve, points=150, rank=1)
        Leaderboard.objects.create(user=bruce, points=90, rank=4)
        Leaderboard.objects.create(user=clark, points=100, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
