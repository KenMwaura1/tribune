from django.test import TestCase
from .models import Article, Editor, Tags


# Create your tests here.
class EditorTestClass(TestCase):
    # Setup method
    def setUp(self):
        self.zoo = Editor(first_name="Zoo", last_name="vier", email="zoo@test.com")

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