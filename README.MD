# Flask API serving MongoDB


## Setting environment with VM

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

* Creating database "users"

```mongodb
> use users;
```

* Inserting data into collection "mycol"

```mongodb
> db.mycol.insert({"name":"Mateus", "role":"Firmware Engineer"});
```

* Inserting data into collection "mycol"

```mongodb
> db.mycol.find();
```