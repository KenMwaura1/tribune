from django.db import models
import datetime as dt


# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    @staticmethod
    def show_all_editors():
        return Editor.objects.all()

    def update_editor_first_name(self, value):
        self.first_name = value
        self.save_editor()

    def update_editor_last_name(self, value):
        self.last_name = value
        self.save_editor()

    def update_editor_email(self, value):
        self.email = value
        self.save_editor()


class Tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/')

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        return cls.objects.filter(pub_date=today)

    @classmethod
    def days_news(cls, date):
        return cls.objects.filter(pub_date=date)

    @classmethod
    def search_by_title(cls, search_term):
        return cls.objects.filter(title__icontains=search_term)


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
