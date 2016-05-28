![](http://i.imgur.com/w9HxHbI.png)


### All majors
Returns an array of all majors.

```
/v1/majors/
```

response:
```
[
    {
        "id": 1,
        "name": "Computer Science",
        "slug": "computer-science"
    },
    {
        "id": 2,
        "name": "Math",
        "slug": "math"
    },
    etc...
]
```


### Courses for a major
Returns Courses for a major

```
/v1/computer-science/
```

response:
```
[
    {
        "id": 1,
        "category": "Programming",
        "name": "C++ for Beginners",
        "major": 1
    },
    {
        "id": 2,
        "category": "Programming",
        "name": "Java",
        "major": 1
    },
    etc...
]
```
