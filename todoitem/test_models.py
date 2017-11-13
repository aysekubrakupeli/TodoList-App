from django.test import TestCase
from .models import TodoItem

# Create your tests here.
class TestItemModel(TestCase):
    def test_can_create_an_item_with_just_a_name(self):
        item = TodoItem(name="any name");
        item.save();
        self.assertEqual(item.name, "any name")
        self.assertFalse(item.done)

    def test_can_create_an_item_with_name_and_status(self):
        item = TodoItem(name="any name", done=True);
        item.save();
        self.assertEqual(item.name, "any name")
        self.assertTrue(item.done)
        
    def test_done_item_as_string(self):
        item = TodoItem(name= "An Item", done=True)
        self.assertEqual("An Item (D)", str(item))
        
    def test_item_as_string(self):
        item = TodoItem(name="An Item", done=False)
        self.assertEqual("An Item (N)", str(item))
        
        