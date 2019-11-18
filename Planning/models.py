from django.db import models
from django.conf import settings
from .choices import EXERCISE_TYPES,RECOVERY_TYPE


class Team(models.Model):
    name = models.CharField(max_length=45)
    logo = models.ImageField(default = 'default_pic.png',upload_to = "logo_pics")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name= "player_creator", on_delete = models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    shoe_size = models.FloatField()
    vetemenent_size = models.FloatField()
    number = models.IntegerField()
    post = models.IntegerField()
    foot_of_strong = models.CharField(max_length = 5)
    team = models.ForeignKey(Team, related_name='players',on_delete = models.CASCADE)

    def __str__(self):
        return ("{} {}".format(self.user.first_name,self.user.last_name))

class Exercise(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,blank=True,null=True )
    exercise_name = models.CharField(max_length = 45)
    exercise_type = models.CharField(max_length = 45 ,choices = EXERCISE_TYPES)
    width = models.FloatField()
    height = models.FloatField()
    duration = models.FloatField()
    sequences = models.FloatField()
    recovery = models.FloatField()
    recovery_type  = models.CharField(max_length = 45 , choices = RECOVERY_TYPE)
    NMI = models.IntegerField()
    effort_perception = models.IntegerField()

class Session(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete= models.CASCADE)
    session_date = models.DateTimeField()
    exercises = models.ManyToManyField(Exercise)


class Question(models.Model):
	question_label = models.CharField(max_length= 255)
	question_text  = models.TextField()
	question_scale = models.PositiveIntegerField()
	question_positive = models.BooleanField()

	def __str__(self):
		return self.question_label

class Survey(models.Model):
	timing_choices = (
			("Anterior","Anterior"), 
			("Posterior","Posterior")
		)
	survey_label = models.CharField(max_length= 255)
	survey_questions = models.ManyToManyField(Question)
	survey_timing = models.CharField(max_length = 20, choices= timing_choices)

	def __str__(self):
		return self.survey_label

class Answer(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    session = models.ForeignKey(Session, on_delete = models.CASCADE)
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    question_answer = models.FloatField()
    answer_valid = models.BooleanField(default = True)

    def __str__(self):
        return self.question_answer
        
    class Meta:
        unique_together = ('player','session','question')



