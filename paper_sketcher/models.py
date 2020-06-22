from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    Degree = (
        ('Doctoral', 'Doctoral'),
        ('Masters', 'Masters'),
        ('Honors', 'Honors'),
    )
    Domain=(
        ('Computer Science', 'Computer Science'),
        ('Information Systems', 'Information Systems'),
    )
    Paper=(
        ('Proposal Paper', 'Proposal Paper'),
        ('Research Paper', 'Research Paper'),
        ('Thesis Paper', 'Thesis Paper'),
       
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level_of_knowledge = models.TextField(max_length=500,choices=Degree, blank=True)
    domain_of_Knowledge = models.CharField(max_length=500, choices=Domain, blank=True)
    type_of_paper = models.CharField(max_length=500, choices=Paper, blank=True)
 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class CS_Research_Paper(models.Model):
    author = models.CharField(max_length = 250, null = True)
    title =  models.TextField(max_length=500, blank=True)
    keywords =  models.TextField(max_length=500, blank=True)
    abstract = models.TextField(max_length=500, blank=True)
    introduction = models.TextField(max_length=500, blank=True)
    background = models.TextField(max_length=500, blank=True)
    methodology = models.TextField(max_length=500, blank=True)
    results = models.TextField(max_length=500, blank=True)
    evaluation = models.TextField(max_length=500, blank=True)
    conclusion = models.TextField(max_length=500, blank=True)
    acknowledgement = models.TextField(max_length=500, blank=True)
    references = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title

     
class CS_Proposal(models.Model):
    author = models.CharField(max_length = 250, null = True)
    title = models.TextField(max_length=500, blank=True)
    table_of_contents = models.TextField(max_length=500, blank=True)
    list_of_figures = models.TextField(max_length=500, blank=True)
    abstract = models.TextField(max_length=500, blank=True)
    introduction = models.TextField(max_length=500, blank=True)
    literature_review = models.TextField(max_length=500, blank=True)
    methodology = models.TextField(max_length=500, blank=True)
    plan = models.TextField(max_length=500, blank=True)
    conclusion = models.TextField(max_length=500, blank=True)
    references = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class CS_Thesis(models.Model):
    author = models.CharField(max_length = 250, null = True)
    title = models.TextField(max_length=500, blank=True)
    abstract = models.TextField(max_length=500, blank=True)
    introduction = models.TextField(max_length=500, blank=True)
    literature_review = models.TextField(max_length=500, blank=True)
    methodology = models.TextField(max_length=500, blank=True)
    results = models.TextField(max_length=500, blank=True)
    evaluation = models.TextField(max_length=500, blank=True)
    conclusion = models.TextField(max_length=500, blank=True)
    references = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class IS_Thesis(models.Model):
    author = models.CharField(max_length = 250, null = True)
    title = models.TextField(max_length=500, blank=True)
    abstract = models.TextField(max_length=500, blank=True)
    introduction = models.TextField(max_length=500, blank=True)
    literature_review = models.TextField(max_length=500, blank=True)
    methodology = models.TextField(max_length=500, blank=True)
    results = models.TextField(max_length=500, blank=True)
    evaluation = models.TextField(max_length=500, blank=True)
    conclusion = models.TextField(max_length=500, blank=True)
    references = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class IS_Proposal(models.Model):
    author = models.CharField(max_length = 250, null = True)
    title = models.TextField(max_length=500, blank=True)
    background = models.TextField(max_length=500, blank=True)
    problem_statement = models.TextField(max_length=500, blank=True)
    objectives = models.TextField(max_length=500, blank=True)
    primary_objectives = models.TextField(max_length=500, blank=True)
    secondary_objectives = models.TextField(max_length=500, blank=True)
    research_questions = models.TextField(max_length=500, blank=True)
    research_significance = models.TextField(max_length=500, blank=True)
    literature_review = models.TextField(max_length=500, blank=True)
    theoretical_paradigm = models.TextField(max_length=500, blank=True)
    research_constructs = models.TextField(max_length=500, blank=True)
    variables_relationship =models.TextField(max_length=500, blank=True)
    methodology = models.TextField(max_length=500, blank=True)
    population_and_sample = models.TextField(max_length=500, blank=True)
    plan = models.TextField(max_length=500, blank=True)
    data_collection = models.TextField(max_length=500, blank=True)
    data_analysisprocedures = models.TextField(max_length=500, blank=True)
    report = models.TextField(max_length=500, blank=True)
    time_frame_budget_considerations = models.TextField(max_length=500, blank=True)
    references = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title

      
class IS_Research_Paper(models.Model):
    author = models.CharField(max_length = 250, null = True)
    title = models.TextField(max_length=500, blank=True)
    abstract = models.TextField(max_length=500, blank=True)
    introduction_and_background = models.TextField(max_length=500, blank=True)
    literature_review = models.TextField(max_length=500, blank=True)
    methodology = models.TextField(max_length=500, blank=True)
    data_analysis = models.TextField(max_length=500, blank=True)
    results_and_discussion = models.TextField(max_length=500, blank=True)
    conclusion = models.TextField(max_length=500, blank=True)
    references = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    
      
      
