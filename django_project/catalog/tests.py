from django.test import TestCase, Client


class StaticURLTests(TestCase):
    # True test
    def test_catalog_item_list(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_detail_numbers(self):
        numbers = [1, 2, 3123, 4, 98, 6234, 7444, 80, 999999999]
        for i in numbers:
            response = Client().get(f'/catalog/{i}/')
            self.assertEqual(response.status_code, 200)

    # test errors
    def test_negative_numbers(self):
        number = -10
        response = Client().get(f'/catalog/{number}')
        self.assertEqual(response.status_code, 404)

    def test_float_numbers(self):
        number = 3.1415
        response = Client().get(f'/catalog/{number}')
        self.assertEqual(response.status_code, 404)

    def test_null_number(self):
        number = 0
        response = Client().get(f'/catalog/{number}')
        self.assertEqual(response.status_code, 404)

    def test_catalog_item_detail_string(self):
        string = 'test_string'
        response = Client().get(f'/catalog/{string}/')
        self.assertEqual(response.status_code, 404)

    def test_max_values(self):
        values = '123abc123abc'
        response = Client().get(f'/catalog/{values}/')
        self.assertEqual(response.status_code, 404)
