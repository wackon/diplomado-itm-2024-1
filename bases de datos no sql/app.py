import boto3

#Crear cliente para dynamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla = dynamodb.Table('tabla-jorge-alvarez')

#Leer un elemento de la tabla
response = tabla.get_item(Key={'id': '2'})

print(response['Item'])

#Leer todos los elementos de la tabla
response = tabla.scan()

print(response['Items'])


item = {
    "id": "3",
    "nombre": "Francisco Mendez",
    "edad": 35,
    "ciudad": "Medellín"
}

tabla.put_item(Item=item)

#Leer un elemento de la tabla
response = tabla.get_item(Key={'id': '3'})

print("Elemento antes de actualizar", response['Item'])

response = tabla.update_item(
    Key={
        'id': '3'  
    },
    UpdateExpression='SET edad = :val1',  # Expresión de actualización
    ExpressionAttributeValues={
        ':val1': 34  # Nuevo valor para atributo2
    }
)

#Leer un elemento de la tabla
response = tabla.get_item(Key={'id': '3'})

print("Elemento despues de actualizar", response["Item"])