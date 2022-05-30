from django.test import TestCase

# Create your tests here.

from .models import Image, Category, Location


class CategoryTest(TestCase):

    def setUp(self):
        self.category = Category(
            name='Wallpaper'
        )
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class LocationTest(TestCase):

    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class ImageTest(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()
        self.category = Category(name='Coding')
        self.category.save_category()
        self.image_test = Image(name='coffee', description='Coffee, Code, Read',
                                location=self.location, category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    def test_get_image_by_category(self):
        category = 'Coding'
        found_img = self.image_test.get_image_by_category(category)
        self.assertTrue(len(found_img) > 1)

    def test_get_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.get_image_by_location(
            location='Nairobi')
        self.assertTrue(len(found_images) == 1)
