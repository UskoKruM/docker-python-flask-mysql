# Docker + MySQL (Localhost): Conexión entre Contenedor de Docker con MySQL en Local (Localhost)

Aprende a crear una conexión entre una aplicación que corre en un contenedor de Docker y una base de datos existente en un servidor local de MySQL (que se ejecuta en tu Localhost), desde cero y de forma detallada.

<hr/>

Primero, crear un entorno virtual:
### `python -m virtualenv venv`

Para instalar los paquetes necesarios:
### `pip install -r requirements.txt`

Crear imagen de Docker:
### `docker build --force-rm -t flask-api . --no-cache`

Ejecutar contenedor con la imagen creada previamente:
### `docker run --env=SECRET_KEY=************ --env=MYSQL_HOST=host.docker.internal --env=MYSQL_DATABASE=database --env=MYSQL_USER=root --env=MYSQL_PW=****** -p 5000:5000 -d --name FlaskAPI flask-api:latest`

<hr/>

![](./preview1.png)
<br/><br/>
![](./preview2.png)

# 🌍 Por si deseas contactarme 👨‍💻 :

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Oscar_Garcia-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://pe.linkedin.com/in/uskokrum2010)
[![YouTube](https://img.shields.io/badge/YouTube-UskoKruM2010-FF0000?style=for-the-badge&logo=youtube&logoColor=white&labelColor=101010)](https://youtube.com/uskokrum2010)
[![Twitter](https://img.shields.io/badge/Twitter-@uskokrum2010-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white&labelColor=101010)](https://twitter.com/uskokrum2010)
[![Instagram](https://img.shields.io/badge/Instagram-@uskokrum2010-E4405F?style=for-the-badge&logo=instagram&logoColor=white&labelColor=101010)](https://instagram.com/uskokrum2010)
[![Facebook](https://img.shields.io/badge/Facebook-@uskokrum2010-1877F2?style=for-the-badge&logo=facebook&logoColor=white&labelColor=101010)](https://facebook.com/uskokrum2010)
[![Udemy](https://img.shields.io/badge/Udemy-Oscar_Garcia-EC5252?style=for-the-badge&logo=udemy&logoColor=white&labelColor=101010)](https://www.udemy.com/course/sql-para-administracion-de-bases-de-datos-con-mysql/)
[![Web](https://img.shields.io/badge/My_Website-uskokrum2010.com-14a1f0?style=for-the-badge&logo=dev.to&logoColor=white&labelColor=101010)](https://uskokrum2010.com)
[![Email](https://img.shields.io/badge/uskokrum2010@gmail.com-mi_email_personal-D14836?style=for-the-badge&logo=gmail&logoColor=white&labelColor=101010)](mailto:uskokrum2010@gmail.com)