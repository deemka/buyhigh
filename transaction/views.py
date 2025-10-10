from rest_framework.viewsets import ModelViewSet

from transaction.models import Transaction


class TransactionViewSet(ModelViewSet):
    model = Transaction

    def list(self, request, *args, **kwargs):
        queryset = Transaction.objects.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)

