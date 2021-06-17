from django.db import models
from phone_field import PhoneField
from jobseeker.models import Candidate
from user_coustom.models import User_custom
# Create your models here.
class Employer(models.Model):
    user = models.ForeignKey(User_custom, null=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"


    # password = models.CharField(max_length=32,widget=forms.PasswordInput)


class Employer_profile(models.Model):
    employer =  models.ForeignKey(Employer,on_delete=models.CASCADE)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    company_type = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    company_logo = models.ImageField()

class Employer_jobs(models.Model):
    employer_id = models.ForeignKey(Employer,on_delete=models.CASCADE)
    job_id = models.IntegerField(primary_key=True)
    job_title = models.CharField(max_length=1250)
    job_description = models.CharField(max_length=1250)
    employment_type = models.CharField(max_length=250)
    job_location = models.CharField(max_length=250)
    job_experience = models.CharField(max_length=250)
    job_savelater = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

class Employer_jobquestions(models.Model):
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    question_id = models.IntegerField(primary_key=True)
    job_id = models.ForeignKey(Employer_jobs,on_delete=models.CASCADE)
    question = models.CharField(max_length=1250)

class Employer_candidate_jobanswer(models.Model):
    candidate_id = models.ForeignKey(Candidate,models.CASCADE)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)

    job_id = models.ForeignKey(Employer_jobs, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Employer_jobquestions,on_delete=models.CASCADE)
    answer = models.CharField(max_length=1250)

class Employer_job_responses(models.Model):
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Employer_jobs,on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate,models.CASCADE)
class Employer_expired_jobs(models.Model):
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Employer_jobs, on_delete=models.CASCADE)
    id= models.IntegerField(primary_key=True)