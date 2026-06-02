# API REST Serverless en AWS

API REST serverless construida 100% sobre la capa gratuita de AWS. Permite crear y listar tareas, con autenticación de usuarios mediante tokens JWT.

Proyecto desarrollado como práctica para la certificación **AWS Certified Cloud Practitioner** y como pieza de portafolio para roles junior de Cloud / DevOps.

## Arquitectura

```
Cliente  ──►  API Gateway  ──►  Lambda (Python)  ──►  DynamoDB
                   ▲
                   │ valida token
                Cognito
```

- **API Gateway** — expone la API a internet y valida los tokens en cada pedido.
- **AWS Lambda (Python)** — ejecuta la lógica: crea tareas (POST) y las lista (GET).
- **DynamoDB** — base de datos NoSQL serverless donde se almacenan las tareas.
- **Amazon Cognito** — autenticación de usuarios. Sin token válido, la API responde 401.

## Endpoints

| Método | Acción | Respuesta |
|--------|--------|-----------|
| `POST` | Crea una tarea (recibe `{ "texto": "..." }`) | `201 Created` |
| `GET` | Lista todas las tareas | `200 OK` |

Todos los endpoints requieren un token válido de Cognito en el header `Authorization`.

## Servicios de AWS utilizados

- AWS Lambda
- Amazon API Gateway (HTTP API)
- Amazon DynamoDB
- Amazon Cognito (User Pool)
- IAM (roles y permisos con principio de menor privilegio)
- AWS Budgets (control de costos)

## Conceptos aplicados

- Arquitectura serverless y modelo de pago por uso.
- Diseño de API REST con métodos HTTP.
- Autenticación basada en tokens (JWT).
- Modelo de responsabilidad compartida y gestión de permisos con IAM.
- Operación dentro de la capa gratuita de AWS.

## Mejoras futuras

- Restringir el rol de Lambda a permisos mínimos sobre la tabla (least privilege).
- Separar la lógica en funciones Lambda independientes por endpoint.
- Agregar endpoints PUT (actualizar) y DELETE (borrar).
- Infraestructura como código con AWS SAM.
- Pipeline de CI/CD con GitHub Actions.

---

Desarrollado por [Lisandro-LMV](https://github.com/Lisandro-LMV)
