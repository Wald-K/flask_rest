import requests

BASE_URL = "http://127.0.0.1:5000/"

# create video
# res = requests.post(BASE_URL + "/video", \
#     {"name":"Blue sky", "views":200, "likes":130})
# print(res.json())


# get all videos
# res = requests.get(BASE_URL + "/video")
# print(res.json())

# get one object
res = requests.get(BASE_URL + "/video/3")
print(res.json())

# delete object
# res = requests.delete(BASE_URL + "/video/2")
# print(res.json())

# update object
# res = requests.put(BASE_URL + "/video/3", {"name":"Blue changed changed", "views":2, "likes":1})
# print(res.json())
