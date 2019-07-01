# py-ziojson
python json serializer

## Example

```
user = User(name='Tom', age=15, gender='man', friends=['Jerry', 'Rose'], pet=Pet('Dog'))
user.id = 1
user.other = {'job': 'Programmer', 'hobby': 'guitar'}
print('\n----- single obj -----\n')
print(make_json_str(user))
print('\n----- obj list -----\n')
print(make_json_str([user, user, user]))
```

```
----- single obj -----

{"age": 15, "friends": ["Jerry", "Rose"], "gender": "man", "id": 1, "name": "Tom", "other": {"job": "Programmer", "hobby": "guitar"}, "pet": {"name": "Dog"}}

----- obj list -----

[{"age": 15, "friends": ["Jerry", "Rose"], "gender": "man", "id": 1, "name": "Tom", "other": {"job": "Programmer", "hobby": "guitar"}, "pet": {"name": "Dog"}}, {"age": 15, "friends": ["Jerry", "Rose"], "gender": "man", "id": 1, "name": "Tom", "other": {"job": "Programmer", "hobby": "guitar"}, "pet": {"name": "Dog"}}, {"age": 15, "friends": ["Jerry", "Rose"], "gender": "man", "id": 1, "name": "Tom", "other": {"job": "Programmer", "hobby": "guitar"}, "pet": {"name": "Dog"}}]

```

