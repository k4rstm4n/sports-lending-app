from django.contrib.auth.models import Group
from allauth.account.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def add_to_borrowers_group(request, user, **kwargs):
    borrowers_group, _ = Group.objects.get_or_create(name="Borrowers")

    if not user.groups.filter(name="Borrowers").exists():
        user.groups.add(borrowers_group)