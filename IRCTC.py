import requests


class IRCTC:
    def __init__(self):
        user=input("""ENTER YOUR CHOICE
        1.Enter 1 to check live train status
        2.Enter 2 to check PNR
        3.Enter 3 to check schedule""")
        if user=="1":
            print("LIVE TRAIN")
        elif user=="2":
            print("CHECK PNR")
        else:
            self.train_schedule()
    def train_schedule(self):
        train_no=input("Enter train number")
        self.fetch_data(train_no)
    def fetch_data(self,train_no):
        headers = {
            "content-type": "application/octet-stream",
            "X-RapidAPI-Key": "cf22b3a36fmsh20b00b7a485c074p15eaa5jsnb923d2ed671f",
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }
        data=requests.get(url="https://irctc1.p.rapidapi.com/api/v1/getTrainSchedule",headers=headers,params={"trainNo":train_no}).json()
        for i in data["data"]["route"]:
            print(i["state_name"])


obj=IRCTC()