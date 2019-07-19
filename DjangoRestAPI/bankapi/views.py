from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Bank, Branch
from .serializers import BranchSerializer
from rest_framework.permissions import IsAuthenticated
import inspect
import json
#from rest_framework.pagination import LimitOffsetPagination
#from rest_framework.generics import ListAPIView



class fyleAPI (APIView):
    permission_classes = (IsAuthenticated,)
    #pagination_class = LimitOffsetPagination
    def get (self, request):
        branches = None
        try:
            if request.GET.getlist('ifsc'):
                ifsc_code = request.GET['ifsc']
                branches = Branch.objects.filter (ifsc = ifsc_code)
                serializer = BranchSerializer (branches, many = True)
                return Response (serializer.data)

            elif request.GET.getlist('bank'):
                req = request.GET['bank']
                req = req.split('/')
                b = req[0]
                c = req[1][5:]
                id = None
                id = Bank.objects.get(name=b)
                branches = Branch.objects.filter (bank_id = id, city = c)
                serializer = BranchSerializer (branches, many = True)
                #content={'message':serializer.data}
                #return Response (content)
                return Response (serializer.data)

        except Exception as e:
            print(e.message,"\t",e.args)
            print("\n\n Server Side issue \n\n")
            pass

    def post (self, request, bank_name = None, city_name = None):
        pass
