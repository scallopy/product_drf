from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer


class TodoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    # get list:
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.filter(user=request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    def get_object(self, todo_id, user_id):
        try:
            return Todo.objects.get(id=todo_id, user=user_id)
        except Todo.DoesNotExist:
            return None

    def get(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": f"Object with todo id: {todo_id} does not extists!"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data)

    def put(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": f"Object with todo id: {todo_id} does not extists!"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(
            instance=todo_instance,
            data=request.data,
            context={'request': request},
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": f"Object with todo id: {todo_id} does not extists!"},
                status=status.HTTP_404_NOT_FOUND
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
