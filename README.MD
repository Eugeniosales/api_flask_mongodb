# Python Crud

This project aims to serve a MongoDB eith a Flask API CRUD and deploy it.

## Tools

* It is necessary to get Postman in Ubuntu Software, to test the API routes

## Setting up environment with Virtualenv

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

* Download MongoDB Shell

    * Follow: <a href="https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu-tarball/">Install mongo shell</a>

### Initializing Mongo shell

* Development

```bash
$ mongo
```

* Production

    * To initialize the Mongo Prod environment, it takes to get the Atlas connection


### Creating Database

* Creating database "users"

```mongodb
> use users;
```

* Removing a database

```mongodb
> db.dropDatabase();
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

* <a href="https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu-tarball/">Install mongo shell</a>
* <a href="https://flask.palletsprojects.com/en/1.1.x/quickstart/#">Flask quickstart</a>
* <a href="https://www.w3schools.com/python/python_mongodb_getstarted.asp">Pymongo Driver</a>
* <a href="https://flask-pymongo.readthedocs.io/en/latest/">Alternative syntax - Flask Pymongo driver</a>