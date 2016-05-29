import subprocess
import uuid
import json

from app.models import Server, Application
from app.serializers import (
    ApplicationSerializer,
    GroupSerializer,
    UserSerializer,
    ServerSerializer
)

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows servers to be viewed or edited.
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    @detail_route()
    def deploy_database(self, request, pk=None):
        application = Application.objects.get(pk=pk)
        
        logPaths = []
        for server in application.servers.all():
            hash = uuid.uuid4().hex
            logPath = '/tmp/deploy-db-{}.log'.format(hash)
            logPaths.append(logPath)
            subprocess.call('cd bin/database-mysql/;./deploy-database.sh {} {} > {} 2>&1 &'.format(
                application.database,
                server.ip,
                logPath
            ), shell=True)

        return Response(json.dumps({'paths': logPaths}))

    @detail_route()
    def deploy(self, request, pk=None):
        application = Application.objects.get(pk=pk)

        logPaths = []
        for server in application.servers.all():
            hash = uuid.uuid4().hex
            logPath = '/tmp/deploy-{}.log'.format(hash)
            logPaths.append(logPath)
            subprocess.call('cd bin;./deploy-web.sh {} {} {} {} > {} 2>&1 &'.format(
                application.path,
                server.path,
                server.ip,
                'vagrant',  # move it into configuration
                logPath
            ), shell=True)

        return Response(json.dumps({'paths': logPaths}))
