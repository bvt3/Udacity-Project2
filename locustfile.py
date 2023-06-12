from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time=between(1, 5)
    host="https://benprj2.azurewebsites.net"

    @task
    def currTest(self):
        self.client.get("/")