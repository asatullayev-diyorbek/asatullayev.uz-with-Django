from django.shortcuts import render
from django.views.generic import View


class HomePageView(View):
    def get(self, request):
        context = {
            'title': "Bosh sahifa",
        }
        return render(request, 'public_panel/base.html', context)
