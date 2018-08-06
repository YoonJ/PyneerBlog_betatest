from django.db import models
from django.utils import timezone

class Project(models.Model):
    #프로젝트 제목입니다
    project_title = models.TextField()
    #프로젝트 내용입니다
    project_text = models.TextField()
    #프로젝트 날짜입니다. 수정해서 해당 년도-학기로 분류할겁니다
    project_date = models.DateTimeField(
        blank=True, null=True)
    project_year_semester = models.TextField()
    project_member = models.TextField()
    project_year = models.TextField()

    def project_year_semester(self):
        if self.project_date.month >= 1 & self.project_date.month <= 6:
            semester = 1
        elif self.project_date.month >= 7 & self.project_date.month <= 12:
            semester = 2
        else:
            semester = 3
        return str(self.project_date.year) + '-' + str(semester)

    def project_year(self):
        return str(self.project_date.year)

    def publish(self):
        self.project_date = timezone.now()
        self.save()

    def __str__(self):
        return self.project_title


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
