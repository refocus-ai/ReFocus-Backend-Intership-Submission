from django.shortcuts import render
from application.models import Company
from rest_framework.views import status, APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict

# Create your views here.
class CompanyCreateUpdateView(APIView):
    """Class for company endpoints."""

    def post(self, request):
        """Create company.

        POST /company
        """
        try:
            company = Company.objects.create(**request.data)
            return Response(status=status.HTTP_201_CREATED, data=model_to_dict(company))
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))


    def patch(self, request):
        """Update existing company.

        PATCH /company
        """
        try:
            company = Company.objects.get(id=request.data["id"])
            company.example_field = request.data["example_field"]
            company.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))
            

class CompanyGetDestroyView(APIView):
    """Class for company endpoints."""

    def get(self, request, *args, **kwargs):
        """Retrieve company.

        GET /company/id
        """
        print(kwargs)
        company_id = kwargs["id"]
        try:
            company = Company.objects.get(id=company_id)
            return Response(status=status.HTTP_200_OK, data=model_to_dict(company))
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))

    def delete(self, request, *args, **kwargs):
        """Delete company.

        DELETE /company/id
        """
        company_id = kwargs["id"]
        try:
            company = Company.objects.get(id=company_id)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))
