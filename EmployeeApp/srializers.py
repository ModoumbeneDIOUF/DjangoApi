from rest_framework import serializers
from EmployeeApp.models import Departements,Employee


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departements
        fields=("DepartementId","DepartementName")



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=("EmployeeId","EmployeeName","Departement","DateOfJoint","PhotoFilName")