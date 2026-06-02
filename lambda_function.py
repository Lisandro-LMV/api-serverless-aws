import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
tabla = dynamodb.Table("Tareas")

def lambda_handler(event, context):
    metodo = event["requestContext"]["http"]["method"]

    if metodo == "POST":
        cuerpo = json.loads(event["body"])
        nueva_tarea = {
            "id": str(uuid.uuid4()),
            "texto": cuerpo["texto"],
            "completada": False
        }
        tabla.put_item(Item=nueva_tarea)
        return {
            "statusCode": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"mensaje": "Tarea creada", "tarea": nueva_tarea})
        }

    elif metodo == "GET":
        respuesta = tabla.scan()
        tareas = respuesta["Items"]
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"tareas": tareas})
        }

    else:
        return {
            "statusCode": 405,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"mensaje": "Metodo no permitido"})
        }