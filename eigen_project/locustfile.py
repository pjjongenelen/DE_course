from locust import HttpLocust, TaskSet, task
from locust.events import request_failure
import json


class WebsiteTasks(TaskSet):
    # training as task
    @task
    def train(self):
        self.client.post("/posts", json=
        {
            "Name": "Ko Tae Won",
            "Age": 25,
            "Value": 400000,
            "Wage": 1000,
            "Preferred_Foot": "Right",
            "Weak_Foot": 3,
            "Trick_Skills": 2,
            "Work_Rate": "Medium/ High",
            "Position": "CB",
            "Jersey_Number": 57,
            "Contract_Valid_Until": "Dec 31, 2019",
            "Height": 188,
            "Weight": 80,
            "Striker": 44,
            "CentralMidfielder": 46,
            "SideMidfielder": 44,
            "WingBack": 54,
            "CenterBack": 62,
            "Crossing": 26,
            "Finishing": 33,
            "HeadingAccuracy": 64,
            "ShortPassing": 56,
            "Volleys": 23,
            "Dribbling": 34,
            "Curve": 25,
            "FreeKickAccuracy": 22,
            "LongPassing": 52,
            "BallControl": 47,
            "Acceleration": 65,
            "SprintSpeed": 61,
            "Agility": 64,
            "Reactions": 61,
            "ShotPower": 31,
            "Jumping": 63,
            "Stamina": 61,
            "Strength": 71,
            "LongShots": 20,
            "Aggression": 63,
            "Interceptions": 64,
            "Positioning": 31,
            "Vision": 26,
            "Penalties": 30,
            "Composure": 59,
            "Marking": 56,
            "StandingTackle": 66,
            "SlidingTackle": 63,
            "Work_Rate_A": "Medium",
            "Work_Rate_D": "High",
            "Position_cat": 3,
            "Basic_Player": 0,
            "Position_Stat": 62
        }
        )
        json_var = response.json()
        request_id = json_var['Name']

        print('Post title is ' + request_id)


            # "/",
            # data=json.dumps({'query': '{findListings {id name}}'}),
            # headers = {'content-type': 'application/json'})

    # # predict as task
    # @task(2)
    # def create_database(self):
    #     self.client.post(
    #     @ task(3)
    #
    # def fill_database(self):
    #


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_mait = 15000


