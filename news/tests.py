from django.test import TestCase
from .models import Article, Editor, Tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):
    # Setup method
    def setUp(self):
        self.zoo = Editor(first_name="Zoo", last_name="vier", email="zoo@test.com")
        self.zoo.save_editor()

        # Creating and saving a new tag
        self.new_tag = Tags(name="testing")
        self.new_tag.save()

        self.new_article = Article(title="Test Article", post=" This is a random test post", editor=self.zoo)
        self.new_article.save()
        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.zoo, Editor))

    def test_save_method(self):
        self.zoo.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_method(self):
        self.zoo.save_editor()
        self.zoo.delete_editor()
        editors = self.zoo.show_all_editors()
        self.assertTrue(len(editors) == 0)

    def test_update_first_name(self):
        self.zoo.save_editor()
        self.zoo.update_editor_first_name("Ken")
        self.assertTrue(self.zoo.first_name == "Ken")

    def test_update_last_name(self):
        self.zoo.save_editor()
        self.zoo.update_editor_last_name("Mwaura")
        self.assertTrue(self.zoo.last_name == "Mwaura")

    def test_update_email(self):
        self.zoo.save_editor()
        self.zoo.update_editor_email("kemwaura@gmail.com")
        self.assertTrue(self.zoo.email == "kemwaura@gmail.com")

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)