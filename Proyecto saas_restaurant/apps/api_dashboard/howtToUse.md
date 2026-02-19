1. Detalles del Endpoint
   Método HTTP: GET

URL: http://localhost:8000/api/dashboard/top-dishes/

Seguridad: Requiere Token de Autenticación (Header Authorization: Bearer <token>).

Permisos: Solo usuarios con perfil Employee y rol administrativo (según tu IsRestaurantAdmin).

2. Estructura de la Respuesta (JSON)
   El endpoint retorna un Array de Objetos. Diseñamos esto específicamente para que sea "Plug & Play" con librerías de gráficos como Recharts o Chart.js. No necesitas transformar nada en el frontend.

Ejemplo de respuesta exitosa (HTTP 200):

JSON

[
{
"name": "Hamburguesa Especial",
"value": 150
},
{
"name": "Pizza Margarita",
"value": 89
},
{
"name": "Coca Cola Zero",
"value": 76
},
{
"name": "Tequeños (12 uds)",
"value": 45
},
{
"name": "Ensalada César",
"value": 30
}
]

Si el restaurante es nuevo (sin ventas): Retorna [] (Array vacío).
