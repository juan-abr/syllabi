from django.urls import path

from .views import *

app_name = 'syllabi'

urlpatterns = [
    path('', RankListView.as_view(), name = 'rank_list_view'),
    # path('rank/<int:rank_id>/', RankDetailView.as_view(), name = 'rank_detail_view'),
    path('<slug>/', RankDetailView.as_view(), name = 'rank_detail_view'),
    path('rank/<int:rank_id>/category/<int:category_id>/requirement/<int:requirement_id>', RequirementDetailView.as_view(), name = 'requirement_detail_view'),
    path('rank/all/', CategoryListView.as_view(), name = 'category_list_view'),
    path('rank/all/category/<int:category_id>/', CategoryDetailView.as_view(), name = 'category_detail_view'),
]