from rest_framework import viewsets


class BaseViewSet(viewsets.GenericViewSet):
    serializer_classes = {}

    def get_serializer_class(self):
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]
        return self.serializer_class
