from django.db import models

# The 6 areas
class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Age categories
class Category(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Below 5 years"

    def __str__(self):
        return self.name

# Events under each category
class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=100)  # e.g., "Smiling Competition"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

# Winners for each event
class Result(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='results')
    position_choices = [(1, '1st'), (2, '2nd'), (3, '3rd')]
    position = models.IntegerField(choices=position_choices, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.event.name} - {self.get_position_display() if self.position else 'Pending'}"
