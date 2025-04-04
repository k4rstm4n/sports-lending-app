from django.contrib.auth.models import Group
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from login.models import Profile
from allauth.socialaccount.models import SocialAccount

@receiver(user_signed_up)
def add_to_borrowers_group(request, user, **kwargs):
    borrowers_group, _ = Group.objects.get_or_create(name="Borrowers")

    if not user.groups.filter(name="Borrowers").exists():
        user.groups.add(borrowers_group)

@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    social_account = SocialAccount.objects.filter(provider="google", user=user).first()
    profile = Profile.objects.create(user=user, 
                        fname=social_account.extra_data["given_name"], 
                        lname=social_account.extra_data["family_name"],
                        email=social_account.extra_data["email"],
                        )
    profile.save()

    