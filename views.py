from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Rank, Category, Requirement

# Create your views here.
class RankListView(ListView):
    model = Rank

class RankDetailView(DetailView):
    model = Rank
    pk_url_kwarg = 'rank_id'


class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category
    pk_url_kwarg = 'category_id'


class RequirementDetailView(LoginRequiredMixin, DetailView):
    model = Requirement
    pk_url_kwarg = 'requirement_id'