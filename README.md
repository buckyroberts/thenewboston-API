![](http://i.imgur.com/w9HxHbI.png)


## All majors

`/v1/majors/` - returns an array of all majors.

request:
```
/v1/majors/
```

response:
```json
[
    {
        "id": 1,
        "name": "Beauty",
        "slug": "beauty"
    },
    {
        "id": 2,
        "name": "Business",
        "slug": "business"
    },
    {
        "id": 3,
        "name": "Computer Science",
        "slug": "computer-science"
    }
]
```


## Courses for a major

`/v1/{major_slug}/` - returns an array of all courses for a major.

request:
```
/v1/computer-science/
```

response:
```json
[
    {
        "id": 1,
        "category": "Programming",
        "name": "AJAX",
        "major": 3
    },
    {
        "id": 2,
        "category": "Programming",
        "name": "Android App Development for Beginners",
        "major": 3
    },
    {
        "id": 3,
        "category": "Programming",
        "name": "C Programming",
        "major": 3
    }
]
```


## Videos for a course

`/v1/videos/{course_id}/` - returns an array of all videos for a course.

request:
```
/v1/videos/1/
```

response:
```json
[
    {
        "episode": 1,
        "title": "Introduction",
        "youtube_code": "QAbQgLGKd3Y",
        "course": 2
    },
    {
        "episode": 2,
        "title": "Installing Android Studio",
        "youtube_code": "zEsDwzjPJ5c",
        "course": 2
    }
]
```

***

Note: the login credentials for the development admin panel are:

- admin
- pass1234
