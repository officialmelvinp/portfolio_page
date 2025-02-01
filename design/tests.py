from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from .models import ContactSubmission
from django.conf import settings

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertIn('positions', response.context)
        self.assertEqual(len(response.context['positions']), 6)

    def test_about_page_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')
        self.assertIn('other_skills', response.context)
        self.assertIn('work_experience', response.context)
        self.assertIn('education', response.context)
        self.assertIn('certifications', response.context)
        self.assertIn('projects', response.context)

    def test_contact_page_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact.html')

    def test_contact_page_view_post(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message'
        }
        response = self.client.post(reverse('contact'), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(ContactSubmission.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'New contact form submission from Test User')

    def test_portfolio_page_view(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/portfolio.html')
        self.assertIn('projects', response.context)
        self.assertEqual(len(response.context['projects']), 5)

    def test_portfolio_detail_view(self):
        response = self.client.get(reverse('portfolio_detail', args=['library-api']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/portfolio-details.html')
        self.assertIn('project', response.context)
        self.assertEqual(response.context['project']['title'], 'Library API')

    def test_portfolio_detail_view_404(self):
        response = self.client.get(reverse('portfolio_detail', args=['non-existent-project']))
        self.assertEqual(response.status_code, 404)

    def test_music_portfolio_view(self):
        response = self.client.get(reverse('music_portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/music_portfolio.html')
        self.assertIn('name', response.context)
        self.assertIn('bio', response.context)
        self.assertIn('profile_image', response.context)
        self.assertIn('songs', response.context)
        self.assertEqual(len(response.context['songs']), 5)


class ContactFormTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_page_loads(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact.html')

    def test_contact_form_submission(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message'
        }
        response = self.client.post(reverse('contact'), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')

        # Check that one message has been sent
        self.assertEqual(len(mail.outbox), 1)

        # Check that the message was sent with the correct subject
        self.assertEqual(mail.outbox[0].subject, 'New contact form submission from Test User')

        # Check that the submission was saved to the database
        self.assertEqual(ContactSubmission.objects.count(), 1)
        submission = ContactSubmission.objects.first()
        self.assertEqual(submission.name, 'Test User')
        self.assertEqual(submission.email, 'test@example.com')
        self.assertEqual(submission.message, 'This is a test message')