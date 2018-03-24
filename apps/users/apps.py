from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'
    verbose_name=u'用户信息'

    # def ready(self):
    #     import users.signals