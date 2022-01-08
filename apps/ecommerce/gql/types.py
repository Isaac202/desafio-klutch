from django.contrib.auth import get_user_model
from graphene import relay
import graphene
from graphene.types import interface
from graphene_django import DjangoObjectType
from apps.ecommerce.models import Order, OrderProduct, Product
from apps.users.models import Customer

class ProductType(DjangoObjectType):
    id = graphene.ID(source="pk", required=True)
    class Meta:
        model = Product
        filter_fields = {
            'name': ['exact', 'icontains'],
            'price': ['lt', 'gt']
        }
        fields = ('id', 'name', 'price', 'quantity')
        interfaces = (relay.Node,)

class OrderType(DjangoObjectType):
    id = graphene.ID(source="pk", required=True)

    class Meta:
        model = Order
        fields = ('id', 'customer_id')
        filter_fields = {
            'customer_id': ['exact'],
        }
        interfaces = (relay.Node,)

class OrderProductType(DjangoObjectType):
    id = graphene.ID(source="pk", required=True)

    class Meta:
        model = OrderProduct
        fields = ('id', 'order_id', 'product_name', 'quantity', 'total')
        filter_fields = {
            'order_id': ['exact'],
        }
        interfaces = (relay.Node,)

class CustomerType(DjangoObjectType):
    id = graphene.ID(source="pk", required=True)
    class Meta:
        model = Customer
        filter_fields = {
            "email": ['exact']
        }
        interfaces = (relay.Node,)