# Flask API serving MongoDB


## Setting up environment with VM

* Installing VM

```bash
$ sudo pip3 install virtualenv
```
* Initializing VM

```bash
$ virtualenv -p python3 .env
```

* Initializing VM

```bash
$ source .env/bin/activate
```

* Downloading dependencies

```bash
$ sudo pip3 install -r requirements.txt
```


## MongoDB

### Setting up MongoDB

* Download MongoDB

```bash
$ sudo apt-get install mongodb
```

* Initializing shell

```bash
$ sudo servive mongodb start
```

```bash
$ mongo
```

* Creating User

```mongodb
> db.createUser({
    user: "user",
    pwd: "mateus1234",
    roles: ["readWrite", "dbAdmin"]
});
```

### Creating Database

* Creating database "users"

```mongodb
> use users;
```

* Creating collection

```mongodb
> db.createCollection('customers');
```

* Inserting data into collection "customers"

```mongodb
> db.customers.insert({
    "name": "Ma",
    "last_name": "Alves",
    "age": "24",
    "role": "Firmware Engineer",    
    "games": ["Bomberman", "The Witcher"],
    "contacts": [{"name":"Eugenio", "last_name":"Sales"}] 
});
```

* Inserting multiple data into collection "customers"

```mongodb
> db.customers.insert([{
    "name": "Ana",
    "last_name": "Gonçalves",
    "age": "25",
    "role": "Production Engineer",    
    "games": ["The sims", "Bomba Patch"],
    "contacts": [{"name":"Mateus", "last_name":"Alves"}] 
},
{
    "name": "Eugenio",
    "last_name": "Sales",
    "age": "22",
    "role": "Poor student",    
    "games": ["FIFA 17", "The last of us"],
    "contacts": [{"name":"Ana", "last_name":"Gonçalves"}] 
},
]);
```

* Getting all documents from 'customers' collection

```mongodb
> db.customers.find().pretty();
```

* Getting a specific document from 'customers' collection by the 'name'

```mongodb
> db.customers.find({name: "Mateus"}).pretty();
```

* Removing a document from collection "customers"

```mongodb
> db.customers.remove({name: "Ana"});
```

## Referências

* <a href="https://docs.mongodb.com/manual/reference/method/db.createUser/">Mongo Db create user</a>