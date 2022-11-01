from django.test import TestCase, Client
from django.forms import ValidationError
from catalog.models import Item, Tag, Category


class StaticURLTests(TestCase):
    # True test
    def test_catalog_item_list(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_detail_numbers(self):
        numbers = [1, 2, 3123, 4, 98, 6234, 7444, 80, 999999999]
        for i in numbers:
            response = Client().get(f'/catalog/{i}/')
            self.assertEqual(response.status_code, 200,
                             msg=f'error number: {i}')

    # test errors
    def test_negative_numbers(self):
        number = -10
        response = Client().get(f'/catalog/{number}/')
        self.assertEqual(response.status_code, 404)

    def test_float_numbers(self):
        number = 3.1415
        response = Client().get(f'/catalog/{number}/')
        self.assertEqual(response.status_code, 404)

    def test_null_number(self):
        number = 0
        response = Client().get(f'/catalog/{number}/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_item_detail_string(self):
        string = 'test_string'
        response = Client().get(f'/catalog/{string}/')
        self.assertEqual(response.status_code, 404)

    def test_mix_values(self):
        values = '123abc123abc'
        response = Client().get(f'/catalog/{values}/')
        self.assertEqual(response.status_code, 404)

    def test_symbols_values(self):
        values = '/#$(*&!@#@!!!!&^((")\n'
        response = Client().get(f'/catalog/{values}/')
        self.assertEqual(response.status_code, 404)


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(is_published=True,
                                               name='Тестовая категория',
                                               slug='test-category-slug')
        cls.tag = Tag.objects.create(is_published=True, name='Тестовый тэг',
                                     slug='test-tag-slug')

    def test_unable_one_letter(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(name='Тестовый item',
                             category=self.category)
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count, f'item_count: {item_count}')

    def test_item_with_text(self):
        item_count = Item.objects.count()
        self.item = Item(name='Тестовый item',
                         text='превосходно',
                         category=self.category)
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), not item_count, f'item_count: {item_count}')


