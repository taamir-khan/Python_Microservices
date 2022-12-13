# Python_Microservices

How to run each microservice

Install docker-compose
```bash
docker-compose up --build
```
Then change directory to one of the following microservices and run ``app.py``

If you experience an issue running ``app.py`` with docker-compose active, then it may be best to test without docker-compose

Once ``app.py`` starts a flask instance, open a new terminal anf run one of the corresponding commands:

password:
```bash
curl -d '{ "password" : "xxxxxxxx" }' -X POST http://localhost:9001/check  -H "Content-type: application/json"
```

user_path_auth:
```bash
curl -d '{ "username": "username1", "password" : "password1" }' -X POST http://localhost:9001/verify -H "Content-type: application/json"
```

emailcheck:
```bash
curl -d "{ \"email\" : \"foo@bar\" }" -X POST http://localhost:9000/check
```

role:
```bash
curl -d '{ "email": "user_email", "newRole" : "role_to_add" }' -X POST http://localhost:9002/addrole -H "Content-type: application/json"
```




