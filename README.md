# AirBnB clone - Console: 💻

<img alt="183268975-648aa48a-76f1-486d-8e55-b335e4279a9e.png" src="assets/183268975-648aa48a-76f1-486d-8e55-b335e4279a9e.png" width="720"/>

<hr>

## Description 📚

The AirBnB Console is a command-line interface (CLI) that provides an
interactive environment for managing and interacting with AirBnB objects. It
allows you to create, retrieve, update, and delete instances of various AirBnB
classes, such as User, Place, City, and more.

<img alt="815046647d23428a14ca.png" src="assets/815046647d23428a14ca.png" width="720"/>

<hr>

## Classes 🏢

AirBnB clone utilizes the following classes:

|    Class    | File                            | Attributes                                                                                                                                                                                                                                           | Methods                                               |
|:-----------:|---------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------|
|  BaseModel  | `models/base_model.py`          | - `id` <br/> - `created_at` <br/> - `updated_at`                                                                                                                                                                                                     | - `save` <br/> - `to_json`                            |
| FileStorage | `models/engine/file_storage.py` | - `__file_path` <br/> - `__objects`                                                                                                                                                                                                                  | - `all` <br/> - `new` <br/> - `save` <br/> - `reload` |
|   Amenity   | `models/amenity.py`             | - `name`                                                                                                                                                                                                                                             | None                                                  |
|    City     | `models/city.py`                | - `state_id` <br/> - `name`                                                                                                                                                                                                                          | None                                                  |
|    Place    | `models/place.py`               | - `city_id` <br/> - `user_id` <br/> - `name` <br/> - `description` <br/> - `number_rooms` <br/> - `number_bathrooms` <br/> - `max_guest` <br/> - `price_by_night` <br/> - `latitude` <br/> - `longitude` <br/> - `amenity_ids` <br/> - `amenity_ids` | None                                                  |
|   Review    | `models/review.py`              | - `place_id` <br/> - `user_id` <br/> - `text`                                                                                                                                                                                                        | None                                                  |
|    State    | `models/state.py`               | - `name`                                                                                                                                                                                                                                             | None                                                  |
|    User     | `models/user.py`                | - `email` <br/> - `password` <br/> - `first_name` <br/> - `last_name`                                                                                                                                                                                | None                                                  |

<hr>

## Storage 💾

The above classes are handled by the abstracted storage engine defined in the
_[FileStorage](models%2Fengine%2Ffile_storage.py)_ class.
<br>

Every time the backend is initialized, AirBnB clone instantiates an instance of
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from
any class instances stored in the JSON file `file.json`. As class instances are
created, updated, or deleted, the `storage` object is used to register
corresponding changes in the `file.json`.



<hr>

## Console Usage ⌨️

The AirBnB console can be run both interactively and non-interactively. To run
the console in non-interactive mode, pipe any command(s) into an execution of
the file `console.py` at the command line.

```shell
$ echo "help" | ./console.py 
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the
file `console.py` by itself:

```shell
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```shell
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```shell
$ ./console.py
(hbnb) quit
$
```

```shell
$ ./console.py
(hbnb) EOF
$
```

<hr>

## Console Commands 📋

The AirBnB console supports the following commands:

* `create`: creates a new instance of model (you need to specify class for the
  model)
* `show`: shows information about a model based on id
* `destroy`: delete model
* `all`: display information about all models
* `update`: updates instance based on name, id and attribute
* `quit`: exits

**Examples of use:**

```shell
(hbnb) create User
3db5637d-5df4-44cf-a250-ef2b523946e9
(hbnb) show User 3db5637d-5df4-44cf-a250-ef2b523946e9
[User] (3db5637d-5df4-44cf-a250-ef2b523946e9) {'id': '3db5637d-5df4-44cf-a250-ef2b523946e9', 
       'updated_at': datetime.datetime(2017, 6, 13, 4, 18, 50, 138053), 'created_at': 
       datetime.datetime(2017, 6, 13, 4, 18, 50, 138027)}
(hbnb) destroy User 3db5637d-5df4-44cf-a250-ef2b523946e9
(hbnb) show User 3db5637d-5df4-44cf-a250-ef2b523946e9
** no instance found **
(hbnb)
```

[//]: # (<hr>)

[//]: # (## Testing 📏)

[//]: # (todo)

<hr>

## Author ✍️

- Hüsam Mahmud <[husamahmud](https://github.com/husamahmud)>
