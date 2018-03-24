# -*- coding: utf-8 -*-  
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _
from django.http.response import HttpResponse
from apps.users.models import EmailVerifyRecord, Banner
# from apps.users.models import UserProfile
from xadmin.plugins.actions import BaseActionView

class MyAction(BaseActionView):
    """定制 action"""
    # 这里需要填写三个属性
    action_name = "my_action"    #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
    description = _(u'Test selected %(verbose_name_plural)s')
    #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.

    model_perm = 'change'    #: 该 Action 所需权限

    # 而后实现 do_action 方法
    def do_action(self, queryset):
        # queryset 是包含了已经选择的数据的 queryset
        for obj in queryset:
            # obj 的操作
            pass
        # 返回 HttpResponse
        return HttpResponse(...)

# class UserProfileAdmin(UserAdmin):
#
#     def get_form_layout(self):
#         if self.org_obj:
#             self.form_layout = (
#                 Main(
#                     Fieldset('',
#                              'username', 'password',
#                              css_class='unsort no_title'
#                              ),
#                     Fieldset(_('Personal info'),
#                              Row('first_name', 'last_name'),
#                              'email'
#                              ),
#                     Fieldset(_('Permissions'),
#                              'groups', 'user_permissions'
#                              ),
#                     Fieldset(_('Important dates'),
#                              'last_login', 'date_joined'
#                              ),
#                 ),
#                 Side(
#                     Fieldset(_('Status'),
#                              'is_active', 'is_staff', 'is_superuser',
#                              ),
#                 )
#             )
#         return super(UserAdmin, self).get_form_layout()

class BaseSetting(object):
    enable_themes = True  # 打开主题功能
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "xxx台管理系统"   # 系统名称
    site_footer = "xxx"     # 底部版权栏
    # menu_style = "accordion"    # 将菜单栏收起来
    # global_models_icon={}  图标
    # default_model_icon
    # def get_site_menu(self):
    #     """``FAQ:如何定制系统菜单``\n
    #     用于给子类复写的方法，开发者可以在子类或 OptionClass 中复写该方法，返回自己定义的网站菜单。菜单的格式为::
    #
    #         ({
    #             "title": "菜单标题", "perm": "权限标示",
    #             "icon": "图标的 css class", "url": "菜单url",
    #             "menus": [...]    # 子菜单项
    #         })
    #
    #     菜单项的 ``perm`` 和 ``url`` 如果是基于 Model 的，可以使用 xadmin 提供的便利方法
    #     :meth:`BaseAdminObject.get_model_perm` 和 :meth:`BaseAdminObject.get_model_url`。举例说明创建菜单::
    #
    #         class AdminSettings(object):
    #
    #             def get_site_menu(self):
    #                 return (
    #                     {'title': '内容管理', 'perm': self.get_model_perm(Article, 'change'), 'menus':(
    #                         {'title': '游戏资料', 'icon': 'info-sign', 'url': self.get_model_url(Article, 'changelist') + '?_rel_categories__id__exact=2'},
    #                         {'title': '网站文章', 'icon': 'file', 'url': self.get_model_url(Article, 'changelist') + '?_rel_categories__id__exact=1'},
    #                     )},
    #                     {'title': '分类管理', 'perm': self.get_model_perm(Category, 'change'), 'menus':(
    #                         {'title': '主要分类', 'url': self.get_model_url(Category, 'changelist') + '?_p_parent__isnull=True'},
    #                         {'title': '游戏资料', 'url': self.get_model_url(Category, 'changelist') + '?_rel_parent__id__exact=2'},
    #                     )},
    #                 )
    #
    #         site.register(CommAdminView, AdminSettings)
    #
    #     """
    #     return None
###################   表配置 ###################
class EmailVerifyRecordAdmin(object):
    refresh_times=[3,5]  # 刷新功能
    list_export=['xls','xml','json'] #配置下载菜单
    actions=[MyAction,]                 #aciton 配置
    list_display = ['code', 'email', 'send_type', 'send_time']  #展示
    search_fields = ['code', 'email', 'send_type']  #搜索
    list_filter = ['code', 'email', 'send_type', 'send_time']  #过滤
    model_icon = 'fa fa-address-book-o'

class BannerAdmin(object):
    list_export=['xls','xml','json']
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)