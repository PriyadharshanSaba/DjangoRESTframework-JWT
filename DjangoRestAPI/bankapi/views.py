from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Bank, Branch
from .serializers import BranchSerializer
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        #print("\n\n\n",request,"\n\n\n")
        content = {'message': 'Hello, World!'}
        return Response(content)



class fyleAPI (APIView):
    permission_classes = (IsAuthenticated,)
    def get (self, request):
        branches = None
        try:
            #print("\n\n\n request.GET['ifsc'] \n\n\n")
            ifsc_code = request.GET['ifsc']
            branches = Branch.objects.filter (ifsc = ifsc_code)
            serializer = BranchSerializer (branches, many = True)
            #content = {'message':serializer.data}
            return Response (serializer.data)
            #return Response (content)
        except:
            try:
                b = request.GET['bank']
                c = request.GET['city']
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
