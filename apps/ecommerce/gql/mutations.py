import graphene
from graphene import Mutation
from apps.ecommerce.models import Order, OrderProduct, Product
from apps.ecommerce.gql.input_types import InputOrderType, InputProductType
from apps.ecommerce.gql.types import OrderProductType, OrderType, ProductType
from apps.users.models import Customer

class CreateProduct(Mutation):
    class Arguments:
        input = graphene.Argument(InputProductType)
    
    product = graphene.Field(ProductType)

    def mutate(root, info, input):
        try:
            product = Product(
                name=input.name,
                price=input.price,
                quantity=input.quantity
            )
            product.save()
            return CreateProduct(product=product)
        except:
            raise Exception("There is already a product with this name!")

class CreateOrder(Mutation):
    order = graphene.Field(OrderType)
    products_list = graphene.List(OrderProductType)
    class Arguments:
        input = graphene.Argument(InputOrderType)
    
    def mutate(root, info, input):
        try:
            customer = Customer.objects.get(pk=input.customer_id)
            order = Order(customer_id=customer.id)
            order.save()
            
            products_list = []
            for order_product in input.products_list:
                product = Product.objects.get(pk=order_product.product_id)
                
                if product.quantity < order_product.quantity:
                    raise Exception("There is not enough of this product in the store!")

                product.quantity -= order_product.quantity
                product.save()

                new_product = OrderProduct(
                    order_id = order.id,
                    product_name = product.name,
                    quantity = order_product.quantity,
                    total = order_product.quantity * product.price
                )   
                new_product.save()
                products_list.append(new_product)

                return CreateOrder(order=order, products_list=products_list) 
        except:
            raise Exception("Check your input information!")
