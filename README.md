![](http://i.imgur.com/w9HxHbI.png)


### All majors

`/v1/majors/` - Returns an array of all majors.

request:
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

`/v1/{major_slug}/` - Returns an array of all courses for a major.

request:
`/v1/computer-science/`

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


### Videos for a course

`/v1/videos/{course_id}/` - Returns an array of all videos for a course.

request:
`/v1/videos/1/`

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
