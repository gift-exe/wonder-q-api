from django.db import models
import uuid
# Create your models here.


class TimeBasedModel(models.Model):
    pkid = models.BigAutoField(primary_key=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class QuestionModel(TimeBasedModel):
    question = models.TextField()
    uploaded_file = models.FileField(
        upload_to='questions', null=True, blank=True)

    def __str__(self):
        return self.question


class AnswerModel(TimeBasedModel):
    question = models.ForeignKey(
        QuestionModel, on_delete=models.CASCADE, related_name='questions')
    answer = models.TextField()

    def __str__(self):
        return f"{self.question.question}'s answer"
