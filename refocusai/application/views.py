from django.shortcuts import render
from application.models import Company, RefocusUser, Permissions, DataEntry
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
            
# Endpoint for User
class UserCreateUpdateView(APIView):
    """Class for user endpoints."""

    def post(self, request):
        """Create user.

        POST /user
        """
        try:
            user = RefocusUser.objects.create(**request.data)
            return Response(status=status.HTTP_201_CREATED, data=model_to_dict(user))
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))


    def patch(self, request):
        """Update existing user.

        PATCH /user
        """
        try:
            # updates user's fields
            #user = user.objects.get(id=request.data["id"])
            user.first_name = request.data["first_name"]
            user.last_name = request.data["last_name"]
            user.email_address = request.data["email_address"]
            user.job_title = request.data["job_title"]
            user.last_date = request.data["last_date"]
            user.admin_user = request.data["admin_user"]
            user.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))


# Endpoint for Permission
class PermissionCreateUpdateView(APIView):
    """Class for permissions endpoints."""

    def post(self, request):
        """Create permission.

        POST /permission
        """
        try:
            permission = Permissions.objects.create(**request.data)
            return Response(status=status.HTTP_201_CREATED, data=model_to_dict(permission))
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))

    
    def patch(self, request):
        """Update existing permission.

        PATCH /permission
        """
        try:
            # update permissions fields
            #user = user.objects.get(id=request.data["id"])
            permission.type = request.data["type"]
            permission.name = request.data["name"]
            permission.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))


# Endpoint for Data Entry
class DataEntryCreateUpdateView(APIView):
    """Class for data entry endpoints."""

    def post(self, request):
        """Create data entry.

        POST /data_entry
        """
        try:
            data_entry = DataEntry.objects.create(**request.data)
            return Response(status=status.HTTP_201_CREATED, data=model_to_dict(DataEntry))
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(e))


    def patch(self, request):
        """Update existing data entry.

        PATCH /data_entry
        """
        try:
            # update data entry fields
            #data_entry = DataEntry.objects.get(id=request.data["id"])
            data_entry.name = request.data["type"]
            data_entry.upload_date = request.data["upload_date"]
            data_entry.data = request.data["data"]
            data_entry.save()
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
