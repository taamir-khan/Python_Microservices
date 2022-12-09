# Python_Microservices

How to run each microservice

two_factor:
```bash
curl -d '{ "first_name": "first_name", "code" : "code_sent_to_phone" }' -X POST http://localhost:9003/authorize -H "Content-type: application/json"
```

user_path_auth:
```bash
curl -d '{ "username": "username1", "password" : "password1" }' -X POST http://localhost:9003/verify -H "Content-type: application/json"
```

emailcheck:
```bash
curl -d "{ \"email\" : \"foo@bar\" }" -X POST http://localhost:9000/check
```

role:
```bash
curl -d '{ "email": "user_email", "newRole" : "role_to_add" }' -X POST http://localhost:9002/addrole -H "Content-type: application/json"
```




