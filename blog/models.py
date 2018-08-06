from django.db import models
from django.utils import timezone

class Project(models.Model):
    #제목
    project_title = models.TextField()
    #내용
    project_text = models.TextField()
    #멤버 이름
    project_member = models.TextField(default = "No one")
    #기타정보
    project_extra = models.TextField(default = " ")
    #프로젝트 날짜
    project_date = models.DateTimeField(
        blank=True, null=True)
    #년도-학기
    project_year_semester = models.TextField()
    #년도
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

# models.py 수정하고 forms.py 수정하고,
# admin.py 수정하고,
# python manage.py makemigrations
# python manage.py migrate
# 터미널에서 위의 작업을 실행한다.