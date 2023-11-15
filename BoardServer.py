from locust import HttpUser, task, between
from random import random

class BoardServer(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/users/sign-in", json={"userId": "topojs9",
                                                 "password": "123"})
    @task(3)
    def view_item(self):
        sortStatus = random.choice(["CATEGORIES", "NEWEST", "OLDEST", "HIGHPRICE", "LOWPRICE", "GRADE"])
        name = ''.join(random.choice('AaBb') for _ in range(1))
        self.client.get(f"/search?name={name}&sortStatus={sortStatus}", name="/item")


