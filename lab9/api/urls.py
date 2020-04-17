from django.urls import path
from api.views import company_list, one_company, comp_vacancies, vacancy_list, vacancy_detail, ten_vacancies
from rest_framework_jwt.views import obtain_jwt_token
from api.views import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:id>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:id>/vacancies/', comp_vacancies),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:id>', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten', ten_vacancies)
]