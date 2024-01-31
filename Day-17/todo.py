import requests

from todoclass import ToDo


api_url ="https://jsonplaceholder.typicode.com/todos/"

response = requests.get(api_url)


if(response.status_code ==200):
    
    todolist = response.json()
    td= ToDo(todolist)
    print(td.userId)
    print(td.id)
    print(td.title)
    print(td.completed)
