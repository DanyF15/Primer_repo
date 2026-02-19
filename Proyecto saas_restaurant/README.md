# 🍽️ SaaS Restaurant

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-Enabled-646CFF?logo=vite&logoColor=white)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow)
![License](https://img.shields.io/badge/License-MIT-blue)
![Made by](https://img.shields.io/badge/Made%20by-Leon%20entre%20el%20Cesped%2C%20Dani%2C%20Gabriel-FF69B4)

**SaaS Restaurant** es una plataforma integral desarrollada con **Django Rest Framework** (Backend) y **React + Vite** (Frontend) para la gestión de restaurantes. Permite administrar empleados, clientes y operaciones bajo un modelo de Software as a Service (SaaS).

---

## 🚀 Instalación

Sigue estos pasos para instalar el proyecto en tu entorno local. El proyecto está dividido en Backend (raíz) y Frontend (`restaurant-front`).

### 1. Clonar el repositorio

```bash
git clone [https://github.com/faryluz/saas_restaurant.git](https://github.com/faryluz/saas_restaurant.git)
cd saas_restaurant
```

### 2. Configuración del Backend (Django)

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Realizar migraciones de base de datos
python manage.py migrate

# (Opcional) Crear un superusuario
python manage.py createsuperuser
```

### 3. Configuración del Frontend (React)

```bash
# Entrar al directorio del frontend
cd restaurant-front

# Instalar dependencias de Node
npm install
```

## ▶️ Correr el proyecto

### Terminal 1: Backend
```bash
# Asegúrate de estar en la raíz del proyecto y con el entorno virtual activado
python manage.py runserver
```

### Terminal 2: Frontend
```bash
# Asegúrate de estar en la carpeta restaurant-front
cd restaurant-front
# Iniciar el servidor de desarrollo de Vite
npm run dev
```

 
