from rest_framework.test import APITestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class TestCSVTaskCreate(APITestCase):

    def create_csv_task(self):
        file = SimpleUploadedFile("test.csv", b"file_content", content_type="text/csv")
        sample_data = {"file": file}
        response = self.client.post(reverse('csv_task_list_or_create'), sample_data)
        self.assertEqual(response.status_code, 201)

    def csv_task_empty_file(self):
        sample_data = {"file": ""}
        response = self.client.post(reverse('csv_task_list_or_create'), sample_data)
        self.assertEqual(response.status_code, 400)

    def csv_task_invalid_file(self):
        file = SimpleUploadedFile("test.mp4", b"file_content", content_type="video/mp4")
        sample_data = {"file": file}
        response = self.client.post(reverse('csv_task_list_or_create'), sample_data)
        self.assertEqual(response.status_code, 400)

class TestCSVTaskGet(APITestCase):

    def get_list(self):
        response = self.client.get(reverse('csv_api:csv_task_list_or_create'))
        self.assertEqual(response.status_code, 200)

    def get_wrong_detail(self):
        response = self.client.get(reverse('csv_api:csv_task_detail', kwargs={'task_id': 'wrong_id'}))
        self.assertEqual(response.status_code, 404)

    def get_empty_detail(self):
        response = self.client.get(reverse('csv_api:csv_task_detail', kwargs={'task_id': ''}))
        self.assertEqual(response.status_code, 404)

    def get_detail(self):
        response = self.client.get(reverse('csv_api:csv_task_detail', kwargs={'task_id': 'test_id'}))
        self.assertEqual(response.status_code, 200)
