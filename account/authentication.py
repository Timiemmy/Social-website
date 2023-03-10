from django.contrib.auth.models import User
from account.models import Profile


class EmailAuthBackend:
    """
    Authenticate using an e-mail address.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            # Here the user with the email is retrieved,
            user = User.objects.get(email=username)
            # The password is checked with this builtin .check_password method of the user model.
            if user.check_password(password):
                return user
            return None
        # The DoesNotExist exception is raised if no user is found with the given email
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None  # The MultipleObjectsReturned exception is raised if multiple users are found using thesame email

    def get_user(self, user_id):  # You get a user through the id povided in the user_id parameter
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


# This function creates profile for user who sign up with social.
def create_profile(backend, user, *args, **kwargs):

    Profile.objects.get_or_create(user=user)
