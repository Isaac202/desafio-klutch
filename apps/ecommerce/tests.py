from graphene_django.utils.testing import GraphQLTestCase
import json
class ProductTestCase(GraphQLTestCase):
    input_data = {"name": "Product1", "price": 50.00, "quantity": 10}

    def test_create_new_product(self):
        """
        It should be able to create a new product with name, price and quantity input
        """
        response = self.query(
            """
            mutation CreateProduct($input: InputProductType) {
                createProduct(
                    input: $input
                ) {
                    product {
                        id
                        name
                        price
                        quantity
                    }
                }
            }
            """,
            op_name="CreateProduct",
            input_data=self.input_data
        )

        content = json.loads(response.content)
        product = content['data']['createProduct']['product']

        self.assertResponseNoErrors(response)
        self.assertEqual(product['name'], self.input_data['name'])
        self.assertEqual(product['price'], self.input_data['price'])
        self.assertEqual(product['quantity'], self.input_data['quantity'])
    
    def test_list_all_products(self):
        self.query(
            """
            mutation CreateProduct($input: InputProductType) {
                createProduct(
                    input: $input
                ) {
                    product {
                        id
                        name
                        price
                        quantity
                    }
                }
            }
            """,
            op_name="CreateProduct",
            input_data=self.input_data
        )
        response = self.query(
            """
            query ListProducts {
                allProducts{
                    edges {
                        node {
                            name
                            quantity
                            price
                        }
                    }
                }
            }
            """,
            op_name="ListProducts",
        )

        content = json.loads(response.content)
        products = content['data']['allProducts']['edges']

        self.assertResponseNoErrors(response)
        self.assertEqual(len(products), 1)

