![](http://i.imgur.com/w9HxHbI.png)


### All majors
Returns an array of all majors.

```
/v1/majors/
```

/v1/majors/:
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
Returns an array of all courses for a major.

```
/v1/{major_slug}/
```

__/v1/computer-science/__:
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
Returns an array of all videos for a course.

```
/v1/videos/{course_id}/
```

__/v1/videos/1/__:
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
