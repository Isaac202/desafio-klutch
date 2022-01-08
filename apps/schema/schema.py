import graphene
from graphene import relay
from graphene_django.filter.fields import DjangoFilterConnectionField

from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

from apps.ecommerce.gql.types import CustomerType, OrderProductType, OrderType, ProductType
from apps.ecommerce.gql.mutations import CreateOrder, CreateProduct

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()

class Query(UserQuery, MeQuery, graphene.ObjectType):
    product = relay.Node.Field(ProductType)
    all_products = DjangoFilterConnectionField(ProductType)

    customer = relay.Node.Field(CustomerType)
    all_customers = DjangoFilterConnectionField(CustomerType)

    order = relay.Node.Field(OrderType)
    all_customer_orders = DjangoFilterConnectionField(OrderType)

    orderProduct = relay.Node.Field(OrderProductType)
    all_order_products = DjangoFilterConnectionField(OrderProductType)

class Mutation(AuthMutation, graphene.ObjectType):
    create_product = CreateProduct.Field()
    create_order = CreateOrder.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)