from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Bank, Branch
from .serializers import BranchSerializer
from rest_framework.permissions import IsAuthenticated
import json
#from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



class fyleAPI (APIView):
    permission_classes = (IsAuthenticated,)
    def get (self, request):
        branches = None
        br_list = []
        try:
            if request.GET.getlist('ifsc'):
                ifsc_code = request.GET['ifsc'].split('/')[0]
                branches = Branch.objects.filter (ifsc = ifsc_code)
                serializer = BranchSerializer (branches, many = True)
            elif request.GET.getlist('bank'):
                req = request.GET['bank']
                req = req.split('/')
                b = req[0]
                c = req[1][5:]
                id = None
                id = Bank.objects.get(name=b)
                if len(req) > 2:
                    l = int(req[2][6:])
                    o = int(req[3][7:])
                    branches = Branch.objects.filter (bank_id = id, city = c)[o:l]      #added the offset and limiting value here
                else:
                    l = 0
                    o = 0
                    branches = Branch.objects.filter (bank_id = id, city = c)
                serializer = BranchSerializer (branches, many = True)
            return Response (serializer.data)

        except Exception as e:
            print(e.message,"\t",e.args)
            print("\n\n Server Side issue \n\n")
            pass

    def post (self, request, bank_name = None, city_name = None):
        pass
