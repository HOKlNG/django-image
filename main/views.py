from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.generic.edit import FormView, View
# Create your views here.


def index(request):
    return render(request, 'index.html')


class MyPage(View):
    """

    """
    params = dict()
    template_name = None

    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):

        return JsonResponse({})