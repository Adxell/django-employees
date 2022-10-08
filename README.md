# django-employees

Base de datos postgresql

Requerimientos

- Tener docker y docker compose instalado

Comandos para ejecutar

Correr los contendores

```
docker-compose up -d
```

Hacer las migraciones

```
docker-compose run web python manage.py migrate
```

Crear superuser

```
docker-compose run web python manage.py createsuperuser
```

Nota: crear el usuario para poder ingresar por medio de login
