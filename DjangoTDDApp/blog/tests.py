from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):
    def test_soke_test(self):
        response = self.client.get('/blog')
       
        self.assertIn('<title> Blog< /title>',response.content.decode())
        self.assertTrue(response.content.decode().startswith('<html>'))

