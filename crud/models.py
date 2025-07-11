from django.db import models
from django.utils.timezone import now

# Utility classes

class Occupation(models.TextChoices):
    STUDENT = 'student', 'Student'
    DEVELOPER = 'developer', 'Developer'
    DATA_SCIENTIST = 'data_scientist', 'Data Scientist'
    DBA = 'dba', 'Database Admin'

class CourseMode(models.TextChoices):
    AUDIT = 'audit', 'Audit'
    HONOR = 'honor', 'Honor'

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
    total_learners = models.IntegerField(default=0)
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

# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=CourseMode.choices, default=CourseMode.AUDIT)