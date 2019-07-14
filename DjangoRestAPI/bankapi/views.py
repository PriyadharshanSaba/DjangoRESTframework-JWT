from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Bank, Branch
from .serializers import BranchSerializer
from rest_framework.permissions import IsAuthenticated



class fyleAPI (APIView):
    permission_classes = (IsAuthenticated,)
    def get (self, request):
        branches = None
        #print("\n\n\n",request.GET['city'],"\n\n\n")
        try:
            #print("\n\n\n",request.GET['ifsc'],"\n\n\n")
            ifsc_code = request.GET['ifsc']
            branches = Branch.objects.filter (ifsc = ifsc_code)
            serializer = BranchSerializer (branches, many = True)
            #content = {'message':serializer.data}
            return Response (serializer.data)
            #return Response (content)
        except:
            #print("\n\n\n",request.GET['bank'],"\n\n\n")
            #print("\n\n\n",request.GET['city'],"\n\n\n")
            try:
                req = request.GET['bank']
                req = req.split('/')
                #print("\n\n\n",req[0],"\n",req[1],"\n\n\n")
                b = req[0]
                c = req[1][5:]
                try:
                    id = None
                    id = Bank.objects.get(name=b)
                    branches = Branch.objects.filter (bank_id = id, city = c)
                    serializer = BranchSerializer (branches, many = True)
                    #content={'message':serializer.data}
                    #return Response (content)
                    return Response (serializer.data)
                except:
                    #print("\n\n\n Error here 2 \n\n\n")
                    pass
            except:
                #print("\n\n\n Error here 2 \n\n\n")
                pass
    def post (self, request, bank_name = None, city_name = None):
        pass
