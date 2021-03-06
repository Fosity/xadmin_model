"""xadmin_dfw_model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
# from django.conf.urls import handler400
# from django.conf.urls import handler500
from django.conf import settings
from django.views.static import serve
### xadmin  ####
import xadmin
from users.views import LoginView
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^media/(?P<path>.*)$',serve, {"document_root":settings.MEDIA_ROOT}),

    url(r'^login/$', LoginView.as_view(),name='login'),
]

#### 配置400 500 页面 ####
# handler400=''
# handler500=''

