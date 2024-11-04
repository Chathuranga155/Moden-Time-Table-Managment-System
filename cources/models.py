from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Batch(models.Model):
    batch_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.batch_name} - {self.faculty.name}"

class Degree(models.Model):
    degree_name = models.CharField(max_length=100)
    degree_code = models.CharField(max_length=10)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.degree_name} ({self.degree_code}) - {self.faculty.name}"

class TeacherEvents(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    url = models.URLField()
    color = models.CharField(max_length=7)  # Hex color code

    def __str__(self):
        return self.name
