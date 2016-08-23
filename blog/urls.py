from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =[
    url(r'^$', views.homepage, name='homepage'),
    url(r'^article/$', views.article, name='article'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about' ),
    url(r'^article/(?P<pk>\d+)/detail/$', views.article_detail, name='detail'),
    url(r'^article/(?P<pk>\d+)/edit/$', views.edit, name='edit'),
    url(r'^singup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^set_password/$',views.set_password, name='set_password'),
    url(r'^log_oug/$', views.log_out, name='log_out'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)