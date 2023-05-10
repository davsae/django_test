from rest_framework import serializers
from api.models import Arts_test
from api.models import Orders

class Art_Serializer(serializers.Art_Serializer):
    class Meta:
        model = Arts_test
        fields = ('Referencia', 'Nombre', 'Descripcion','Precio','tax','date')
        
class Orders_Serializer(serializers.Orders_Serializer):
    class Meta:
        model = Orders
        fields = ('Referencia', 'Cantidad', 'Precio_T','Precio_I','tax','date')
        
