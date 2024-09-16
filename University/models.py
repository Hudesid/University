from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name, self.last_name


class Group(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name, self.last_name



