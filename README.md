# Instalación del proyecto


## 1. Clonar el repositorio
Posicionarnos en donde clonaremos el entorno
```
git clone https://github.com/Raymundoo/raynhardt-api.git
```

## 2. Instalar el entorno
#### 2.1 Usaremos virtualenv para crear el entorno
```
mkvirtualenv api-cliente
```
#### 2.2 Levantamos el entorno
El siguiente path es en donde instale mi entorno en su caso deberan poner el path en donde instalaron su entorno
```
source /var/waps/entornos/api-cliente/bin/activate
```

#### 2.3 Nos posicionamos en la raiz del proyecto clonado anteriormente e instalamos los requerimientos
```
pip install -r requirements.txt
```


## 3. Creamos el archivo .env

```
nano prueba/.env
```
Agregamos los siguiente
```
DEBUG=True
ALLOWED_HOSTS=*


# API Rayinhardt
API_USER=usuario que crearon en el proyecto de RaynhardtAPI
API_PASSWORD=usuario que crearon en el proyecto de RaynhardtAPI

```

## 4. Correr el proyecto
```
python manage.py runserver 0.0.0.0:8001
```

## 5. Ingresamos al nevegador con ***http://127.0.0.1:8001/*** para comprobar que el proyecto este corriendo
 