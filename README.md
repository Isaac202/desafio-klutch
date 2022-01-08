# Klutch E-Commerce

This project is part of the admission process at Klutch Tecnologia. The objetie is create a basic ecommerce to deal with customers access, orders and product registration in storage. The project is written in python django with the Graphql API architeture.

You can access the deployed app at [here](https://klutch-ecommerce-challenge.herokuapp.com).

## Technologies

- [python](https://www.python.org/)
- [django](https://www.djangoproject.com/)
- [graphene-django](https://docs.graphene-python.org/projects/django/en/latest/)
- [django-graphql-auth](https://django-graphql-auth.readthedocs.io/en/latest/)
- [django-graphql-jwt](https://django-graphql-jwt.domake.io/en/latest/index.html)
- [django-filter](https://django-filter.readthedocs.io/en/stable/)

## How to Run

After you clone this repository in your machine, get into the project folder, create a virtual enviroment and activate it:

```bash
git clone https://github.com/hereisjohnny2/klutch-ecommerce.git
cd klutch-ecommerce
python -m venv venv
source venv/script/activate
```

All the project requirements are in the file `requirements.txt`. To install then you might use `pip` to do so:

```bash
pip install -r requirements.txt
```

The next step is to run the migrations on the database and create a superuser to work with the django administration panel:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Finally you now can run the project and access the endpoints on the browser to explorer:
```bash
python manage.py runserver
```

## Queries and Mutation

This project uses the [graphene-django]() library to deal with a graphql architecture. To test the queries and mutations and access the documentation you can use the `GraphiQl` testing interface in the `graphql` endpoint. 

```
http://localhost:8000/graphql/
```
### Queries

#### List all products in the store

```graphql
allProducts(
    offset: Int
    before: String
    after: String
    first: Int
    last: Int
    name: String
    name_I
    contains: String
    price_Lt: Float
    price_Gt: Float
) {
    edges {
        node {
            id: ID
            name: String
            price: Float
            quantity: Int
        }
    }
}
``` 

#### Show customer info by its ID

```graphql
customer(
    id: ID
){
    id: ID!
    lastLogin: DateTime
    username: String!
    firstName: String!
    lastName: String!
    isStaff: Boolean!
    isActive: Boolean!
    dateJoined: DateTime!
    email: String!
    password: String!
    isSuperuser: Boolean!   
}
``` 

#### List all customer orders

```graphql
allCustomerOrders(
    offset: Int
    before: String
    after: String
    first: Int
    last: Int
    customerId: Int!
) {
    edges {
        node {
            id: ID!
            customerId: Int!
        }
    }
} 
```

#### List all products in an specific order

```graphql
allOrderProducts(
    offset: Int
    before: String
    after: String
    first: Int
    last: Int
    orderId: Int!
) {
    edges {
        node {
            id: ID!
            orderId: Int!
            productName: String!
            quantity: Int!
            total: Float!
        }
    }
}
```  


### Mutations

#### Create a new customer

```graphql
register(
    email: String!
    username: String!
    password1: String!
    password2: String!
) {
    success: Boolean
    errors: ExpectedErrorType
    token: String
}
```

#### Obtain a JsonWebToken for a customer

```graphql
tokenAuth(
    password: String!
    email: Stringuser
    name: String
) {
    token: String
    success: Boolean
    errors: ExpectedErrorType
    user: UserNode
    unarchiving: Boolean
    refreshToken: String
}
```

#### Create a new product

```graphql 
createProduct(
    input: {
        name: String
        price: Float
        quantity: Int
    }
) {
    product {
        id: ID!
        name: String!
        price: Float!
        quantity: Int!
    }
}
```

#### Create a new order 

```graphql
createOrder(
    input: {
        customerId: Int!
        productList: [
            {
                productId: Int
                quantity: Int
            }
            ...
        ]
    }
) {
    order {
        id: ID!
        customerId: Int!
    }
    productsList: [
        {
            id: ID!
            orderId: Int!
            productName: String!
            quantity: Int!
            total: Float!
        }
    ]
}
```