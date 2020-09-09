from django.db import models

# Create your models here.

# choices for difficulty rating
diff_choices = [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
    ('Expert', 'Expert'),
    ('INSANE', 'INSANE'),
]


# model for tracking bike rides
class MyBikeRides(models.Model):
    trail_network_name = models.CharField(max_length=75, blank=False)
    # drop down of choices from dictionary above
    trail_difficulty = models.CharField(max_length=30, choices=diff_choices)
    miles_ridden = models.DecimalField(default=00.00, max_digits=1000, decimal_places=2)
    date_ridden = models.DateField()
    trail_town = models.CharField(max_length=55, blank=True, null=True)
    trail_state = models.CharField(max_length=4)
    bike_name = models.CharField(max_length=55, blank=True)
    ride_comments = models.CharField(max_length=100, default='', blank=True)

    # change name of entry to trail name on page
    mtb_objects = models.Manager()

    # __str__ method pulls trail name
    def __str__(self):
        return self.trail_network_name
