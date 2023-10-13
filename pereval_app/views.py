from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets, status, generics
from .serializers import *
from .models import *


class PerevalCreateView(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id__email']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pereval_id = serializer.data.get('id')
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Successfully created',
                'id': pereval_id
            }
            return Response(response)
        pereval_id = serializer.data.get('id')
        response = {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors,
            'id': pereval_id
        }
        return Response(response)


class PerevalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer
    http_method_names = ['get', 'patch', 'delete']

    def get_object(self):
        pk = self.kwargs.get('pk')
        pereval = PerevalAdded.objects.get(pk=pk)
        return pereval

    def get(self, request, *args, **kwargs):
        pereval = self.get_object()
        serializer = PerevalFullViewSerializer(pereval)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response = {
                    'state': '1',
                    'message': 'Successfully patched'
                }
                return Response(response)
            response = {
                'state': '0',
                'message': serializer.errors
            }
            return Response(response)
        response = {
            'state': '0',
            'message': "Запись не в статусе 'new'"
        }
        return Response(response)


class UserViewSet(viewsets.ModelViewSet):
    queryset = PerevalUser.objects.all()
    serializer_class = UserSerialiser
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user', request=request, format=format),
        'submitData': reverse('submitData', request=request, format=format)
    })