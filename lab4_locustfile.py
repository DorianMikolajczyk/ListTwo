from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def endpoint1(self):
        self.client.get("/endpoint1")

    @task
    def endpoint2(self):
        self.client.post("/endpoint2", json={"data": "example"})

    @task
    def endpoint3(self):
        self.client.put("/endpoint3/123", json={"data": "example"})

    @task
    def endpoint4(self):
        self.client.delete("/endpoint4/123")

    @task
    def endpoint5(self):
        self.client.get("/endpoint5?param1=value1&param2=value2")