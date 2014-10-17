from django.test import TestCase
from django.core.exceptions import ValidationError
from ..forms import EmailUserCreationForm
from ..models import Player


class FormTestCase(TestCase):
    def setUp(self):
        self.test_name = 'test-user'
        self.test_other_name = 'other-test-user'
        self.user = Player.objects.create_user(username=self.test_name)

    def test_clean_username_exception(self):
        # set up the form for testing
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': self.test_name}

        # use a context manager to watch for the validation error being raised
        with self.assertRaises(ValidationError):
            form.clean_username()

    def test_clean_username_pass(self):
        # set up the form for testing
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': self.test_other_name}

        # use a context manager to watch for the validation error being raised
        self.assertEquals(form.clean_username(), self.test_other_name)
