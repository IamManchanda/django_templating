from django.views.generic import TemplateView

class IndexPageView(TemplateView):
    template_name = 'pages/index.html'

class AboutUsPageView(TemplateView):
    template_name = 'pages/about-us.html'

class ContactUsPageView(TemplateView):
    template_name = 'pages/contact-us.html'
