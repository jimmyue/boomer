from locust import HttpUser,TaskSet,task

class MyTaskSet(TaskSet):
    @task(1)
    def hello(self):
        pass

class WebsiteUser(HttpUser):
	tasks = [MyTaskSet]