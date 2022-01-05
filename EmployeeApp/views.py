from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departements,Employee
from EmployeeApp.srializers import DepartementSerializer,EmployeeSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def departementApi(request,id=0):
    if request.method =='GET':
        departements = Departements.objects.all()
        departements_serializable = DepartementSerializer(departements,many=True)
        return JsonResponse(departements_serializable.data,safe=False)
    elif request.method =='POST':
        deptData = JSONParser().parse(request)
        deptSeria = DepartementSerializer(data=deptData)
        if deptSeria.is_valid():
            deptSeria.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add dept",safe=False)   

    elif request.method == "PUT":
        deptData = JSONParser().parse(request)
        dept = Departements.objects.get(DepartementId=deptData['DepartementId'])
        deptSeria = DepartementSerializer(dept,data=deptData)
        if deptSeria.is_valid():
            deptSeria.save()
            return JsonResponse("Updated successfully",safe=False)         
        return JsonResponse("Added with Error",safe=False)    

    elif request.method == "DELETE":
        dept = Departements(DepartementId=id)
        dept.delete()
        return JsonResponse("Deleted successfully",safe=False)        


@csrf_exempt
def employeeApi(request,id=0):
    if request.method =='GET':
        emp = Employee.objects.all()
        empS = EmployeeSerializer(emp,many=True)
        return JsonResponse(empS.data,safe=False)
    elif request.method =='POST':
        empData = JSONParser().parse(request)
        empS = EmployeeSerializer(data=empData)
        if empS.is_valid():
            empS.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add dept",safe=False)   

    elif request.method == "PUT":
        empData = JSONParser().parse(request)
        emp = Employee.objects.get(EmployeeId=empData['EmployeeId'])
        empS = EmployeeSerializer(emp,data=empData)
        if empS.is_valid():
            empS.save()
            return JsonResponse("Updated successfully",safe=False)         
        return JsonResponse("Added with Error",safe=False)    

    elif request.method == "DELETE":
        emp = Employee(EmployeeId=id)
        emp.delete()
        return JsonResponse("Deleted successfully",safe=False)        


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)  
# Create your views here.
