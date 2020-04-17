from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Vacancy
from django.views import View
from api.serializers import CompanySerializer, VacancySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import json


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({'error': serializer.errors})



@csrf_exempt
def one_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'company does not exist'})
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.body(request.body)
        serializer = CompanySerializer(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': company.name})


@csrf_exempt
def comp_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'company does not exist'})
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id=id)
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        vacancy = Vacancy.objects.create(name=data['name'], description=data['description'], salary=data['salary'],
                                         company_id=id)
        return JsonResponse(vacancy.to_json())


@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({'error': serializer.errors})


@csrf_exempt
def vacancy_detail(request, id):
    if request.method == 'GET':
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist:
            return JsonResponse({'error': 'vacancy does not exist'})
        return JsonResponse(vacancy.to_json(), safe=False)



@csrf_exempt
def ten_vacancies(request):
    if request.method == 'GET':
        top_ten = Vacancy.objects.all().order_by('-salary')[:10]
        top_ten_json = [vacancy.to_json() for vacancy in top_ten]
        return JsonResponse(top_ten_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'error': 'you cannot post here'})


# class CompanyListAPIView(APIView):
#     def get(self, request):
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# class VacancyListAPIView(APIView):
#     def get(self, request):
#         vacancies = Vacancy.objects.all()
#         serializer = VacancySerializer(vacancies, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = VacancySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# class CompanyDetailAPIView(APIView):
#     def get_object(self, id):
#         try:
#             return Company.objects.get(id=id)
#         except Company.DoesNotExist as e:
#             return Response({'error': str(e)})
#
#     def get(self, request, company_id):
#         company = self.get_object(company_id)
#         serializer = CompanySerializer(company)
#         return Response(serializer.data)
#
#     def put(self, request, company_id):
#         company = self.get_object(company_id)
#         serializer = CompanySerializer(instance=company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({'error': serializer.errors})
#
#     def delete(self, request, company_id):
#         company = self.get_object(company_id)
#         company.delete()
#
#         return Response({'deleted': True})
#
#
# class VacancyDetailAPIView(APIView):
#     def get_object(self, id):
#             try:
#                 return Vacancy.objects.get(id=id)
#             except Vacancy.DoesNotExist as e:
#                 return Response({'error': str(e)})
#
#     def get(self, request, vacancy_id):
#             vacancy = self.get_object(vacancy_id)
#             serializer = CompanySerializer(vacancy)
#             return Response(serializer.data)
#
#     def put(self, request, vacancy_id):
#         vacancy = self.get_object(vacancy_id)
#         serializer = CompanySerializer(instance=vacancy, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({'error': serializer.errors})
#
#     def delete(self, request, vacancy_id):
#         vacancy = self.get_object(vacancy_id)
#         vacancy.delete()
#
#         return Response({'deleted': True})


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)


class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
# class CompanyList(View):
#
#     def get(self, request):
#         companies = Company.objects.all()
#         companies_json = [company.brief_json() for company in companies]
#         return JsonResponse(companies_json, safe=False)
#
#     def post(self, request):
#         data = json.loads(request.body)
#         company = Company.objects.create(name=data['name'], description=data['description'], city=data['city'],
#                                          address=data['address'])
#         return JsonResponse(company.to_json())
#
#
# class OneCompany(View):
#     def get(self, request, id):
#         try:
#             company = Company.objects.get(id=id)
#         except Company.DoesNotExist as e:
#             return JsonResponse({'error': 'company does not exist'})
#         return JsonResponse(company.to_json())
#
#
# class CompVacancies(View):
#     def error(self):
#         return JsonResponse({'error': 'company does not exist'})
#
#     def get(self, request, id):
#         try:
#             company = Company.objects.get(id=id)
#         except Company.DoesNotExist:
#             self.error()
#         vacancies = Vacancy.objects.filter(id=id)
#         vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#         return JsonResponse(vacancies_json, safe=False)
#
#     def post(self, request):
#         data = json.loads(request.body)
#         vacancy = Vacancy.objects.create(name=data['name'], description=data['description'], salary=data['salary'],
#                                          company_id=id)
#         return JsonResponse(vacancy.to_json())
#
#
# class VacancyList(View):
#     def get(self, request):
#         vacancies = Vacancy.objects.all()
#         vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#         return JsonResponse(vacancies_json, safe=False)
#
#     def post(self, request):
#         data = json.loads(request.body)
#         vacancy = Vacancy.objects.create(name=data['name'], description=data['description'], salary=data['salary'],
#                                          company_id=data['company_id'])
#         return JsonResponse(vacancy.to_json())
#
#
# class VacancyDetail(View):
#     def get(self, request, id):
#         try:
#             vacancy = Vacancy.objects.get(id=id)
#         except Vacancy.DoesNotExist:
#             return JsonResponse({'error': 'vacancy does not exist'})
#         return JsonResponse(vacancy.to_json(), safe=False)
#
#
# class TopTen(View):
#     def get(self, request):
#         top_ten = Vacancy.objects.all().order_by('-salary')[:10]
#         top_ten_json = [vacancy.to_json() for vacancy in top_ten]
#         return JsonResponse(top_ten_json, safe=False)
#
#     def post(self, request):
#         return JsonResponse({'error': 'you cannot post here'})
