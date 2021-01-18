from django.db import models
from django.db.models.signals import post_save
from django.conf import settings

# 유저에 대한 정보가 별로 없으니 profile을 직접만들어보자!
# 근데 onetoonefield인데, profile model을 생성하고 migrate해버리면
# 기존에 있었던 user들은 profile이 없게 된다!
# 그러면 migrations파일에 들어가서, migrate하자마자 현재 db에 등록되어 있는 user들에 대해서도 만들어주려 한다.
# migrations 파일로 가자. 공식문서 가면 RunPython 부분이 있다.

# 또한 회원가입 동시에 user객체가 만들어지면 profile이 생성되도록 만들어야 한다.
# django post_save, signal을 써보자


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)


def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)


post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)
