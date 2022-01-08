import graphene
from graphene import InputObjectType
class InputOrderProductType(InputObjectType):
    product_id = graphene.Int()
    quantity = graphene.Int()

class InputOrderType(InputObjectType):
    customer_id = graphene.Int()
    products_list = graphene.List(InputOrderProductType)

class InputProductType(InputObjectType):
    name = graphene.String()
    price = graphene.Float()
    quantity = graphene.Int()

