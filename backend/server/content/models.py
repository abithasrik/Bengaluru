from django.db import models

# ---------------- Course Model ----------------
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    specialties = models.JSONField(default=list)  # e.g., ["Frontend", "Backend"]
    course_description = models.TextField()
    mock_interview = models.TextField(blank=True, null=True)
    project = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.course_name

# ---------------- Syllabus Model ----------------
class Syllabus(models.Model):
    course = models.ForeignKey(Course, related_name='syllabus', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    description = models.TextField(help_text="Detailed description shown when accordion is expanded") #changed

    def __str__(self):
        return f"{self.course.course_name} - {self.heading}"

# ---------------- Batch Model ----------------
class Batch(models.Model):
    course = models.ForeignKey(Course, related_name='batches', on_delete=models.CASCADE)
    trainer = models.ForeignKey('Trainer', related_name='batches', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.course.course_name} - {self.date} {self.time}"

# ---------------- Trainer Model ----------------
class Trainer(models.Model):
    name = models.CharField(max_length=150)
    expertise = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

# ---------------- Training Features ----------------

class TrainingFeature(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='training_features')
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='training_features/', blank=True, null=True)

    def __str__(self):
        return f"{self.course.course_name} - {self.title}"

# ---------------- Certification Model ----------------
class Certification(models.Model):
    course = models.ForeignKey(Course, related_name='certifications', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="certification_images/", blank=True, null=True)  # changed

    def __str__(self):
        return f"{self.course.course_name} - {self.heading}"

# ---------------- FAQ Model ----------------
class FAQ(models.Model):
    course = models.ForeignKey(Course, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return f"{self.course.course_name} - {self.question}"

# ---------------- Offer Model ----------------
class Offer(models.Model):
    course = models.ForeignKey(Course, related_name='offers', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discount_percentage = models.IntegerField()
    valid_until = models.DateField()

    def __str__(self):
        return f"{self.course.course_name} - {self.title}"
    

# ---------------- Review Model ---------------

class CourseReview(models.Model):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='review_profiles/', blank=True, null=True)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)  # 1 to 5 stars

    def __str__(self):
        return f"{self.course.course_name} - {self.name} - {self.rating}⭐"
