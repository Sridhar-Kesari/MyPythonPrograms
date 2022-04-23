# def greet():
#     print("Hello")
#
#
# def before_and_after(func):
#     print("Before")
#     func()
#     print("After")
#
#
# before_and_after(greet)

print("---------------")
movies = [
    {"name":"ABC", "dir":"Sri"},
    {"name":"123", "dir":"Kri"},
    {"name":"PPP", "dir":"Vri"},
]

def find_movie(expected, finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie

find_by = input("What property: ")
looking_for = input("what looking for: ")
movie = find_movie (looking_for, lambda movie: movie[find_by])
print(movie or 'No movie found')