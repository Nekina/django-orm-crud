from django.db import models
from django.utils.timezone import now

# Utility classes

class Occupation(models.TextChoices):
    STUDENT = 'student', 'Student'
    DEVELOPER = 'developer', 'Developer'
    DATA_SCIENTIST = 'data_scientist', 'Data Scientist'
    DBA = 'dba', 'Database Admin'

# Model classes

class User(models.Model):
    # Fields
    first_name = models.CharField(null=False, max_length=30, default='John')
    last_name = models.CharField(null=False, max_length=30, default='Doe')
    dob = models.DateField(null=True)
    # Methods
    def __str__(self):
        # Returns the name of a User
        return self.first_name + " " + self.last_name

class Instructor(User):
    # Fields
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField
    # Methods
    def __str__(self):
        return (
            "First name: " + self.first_name +
            ", Last name: " + self.last_name +
            ", Is full time: " + str(self.full_time) +
            ", Total Learners: " + str(self.total_learners)
        )

class Learner(User):
    # Fields
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=Occupation.choices,
        default=Occupation.STUDENT
    )
    social_link = models.URLField(max_length=200)
    # Methods
    def __str__(self):
        return (
            "First name: " + self.first_name +
            ", Last name: " + self.last_name +
            ", Date of Birth: " + str(self.dob) +
            ", Occupation: " + self.occupation +
            ", Social Link: " + self.social_link
        )

class Course(models.Model):
    # Fields
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    instructors = models.ManyToManyField(Instructor)
    # Methods
    def __str__(self):
        return (
            "Name: " + self.name +
            ", Description: " + self.description
        )

class Lesson(models.Model):
    # Fields
    title = models.CharField(max_length=200, default='title')
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()
