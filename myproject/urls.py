"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from boards import views
from django.conf import settings
from django.views.static import serve 



urlpatterns = [ 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    path('slide1/<int:num>/', views.slide1, name='slide1'),    
    url(r'^slide2/', views.slide2, name='slide2'),    
    path('slide3/<int:num>/', views.slide3, name='slide3'),
    path('slide4/<int:num>/', views.slide4, name='slide4'),    
    path('slide5/<int:num>/', views.slide5, name='slide5'),    
    url(r'^slide6/', views.slide6, name='slide6'),
    url(r'^article1/', views.article1, name='article1'),
    url(r'^article2/', views.article2, name='article2'),
    url(r'^article3/', views.article3, name='article3'),
    url(r'^article4/', views.article4, name='article4'),
    url(r'^report1/', views.report1, name='report1'),
    url(r'^report2/', views.report2, name='report2'),
    url(r'^webinar1/', views.webinar1, name='webinar1'),
    url(r'^webinar2/', views.webinar2, name='webinar2'),
    url(r'^webinar3/', views.webinar3, name='webinar3'),
    path('news-sub/<int:num>/', views.news_sub, name='news-sub'),
    url(r'^ScenarioFrontier/', views.ScenarioFrontier, name='ScenarioFrontier'), 
    url(r'^ECAPLeader/', views.ECAPLeader, name='ECAPLeader'),
    url(r'^ModelTek/', views.ModelTek, name='ModelTek'),
    url(r'^MortgageRetainer/', views.MortgageRetainer, name='MortgageRetainer'),
    url(r'^CreditStream/', views.CreditStream, name='CreditStream'),
    url(r'^RetailEdge/', views.RetailEdge, name='RetailEdge'),
    url(r'^BranchScape/', views.BranchScape, name='BranchScape'),
    url(r'^Cyber_security/', views.Cyber_security, name='Cyber_security'),
    url(r'^Regulatory_Compliance/', views.Regulatory_Compliance, name='Regulatory_Compliance'),
    url(r'^Pricing_Profitability/', views.Pricing_Profitability, name='Pricing_Profitability'),
    url(r'^Finance/', views.Finance, name='Finance'),
    url(r'^news/', views.news, name='news'),
    url(r'^events/', views.events, name='events'),
    path('event-sub/<int:num>/', views.events_sub, name='events-sub'),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^contactus/', views.contactus, name='contactus'),
    url(r'^partner/', views.partner, name='partner'),
    url(r'^insights/', views.insights, name='insights'),  
    path('insights-sub/<int:num>/', views.insights_sub, name='insights-sub'),
    url(r'^cookie-notice-and-privacy-policy/', views.cookie, name='cookie-notice-and-privacy-policy'),
    url(r'^GDPR/', views.GDPR, name='GDPR'),
    url(r'^terms/', views.terms, name='terms')
]

