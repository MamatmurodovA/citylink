from django.views.generic import TemplateView

from app.models import Service


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'services': Service.objects.all()
        })
        return ctx
