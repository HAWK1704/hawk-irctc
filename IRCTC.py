import requests


class IRCTC:
    def __init__(self):
        user=input("""ENTER YOUR CHOICE
        1.Enter 1 to check live train status
        2.Enter 2 to check PNR
        3.Enter 3 to check schedule""")
        if user=="1":
            self.live_train()
        elif user=="2":
            self.train_pnr()
        else:
            self.train_schedule()

    def live_train(self):
        train_no=input("Enter train number")
        day=input("Enter the day you want to look in (like 1,2,3...)")
        self.fetch_data3(train_no,day)

    def fetch_data3(self,train_no,day):
        headers = {
            "content-type": "application/octet-stream",
            "X-RapidAPI-Key": "cf22b3a36fmsh20b00b7a485c074p15eaa5jsnb923d2ed671f",
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }
        querystring = {"trainNo": train_no, "startDay": day}
        data=requests.get(url="https://irctc1.p.rapidapi.com/api/v1/liveTrainStatus",headers=headers,params=querystring).json()
        print(data)

    def train_schedule(self):
        train_no=input("Enter train number")
        self.fetch_data1(train_no)

    def train_pnr(self):
        train_pnr=input("Enter PNR number")
        self.fetch_data2(train_pnr)

    def fetch_data2(self,train_pnr):
        headers = {
            "content-type": "application/octet-stream",
            "X-RapidAPI-Key": "cf22b3a36fmsh20b00b7a485c074p15eaa5jsnb923d2ed671f",
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }
        data=requests.get(url="https://irctc1.p.rapidapi.com/api/v3/getPNRStatus",headers=headers,params={"pnrNumber":train_pnr}).json()
        print(data)

    def fetch_data1(self,train_no):
        headers = {
            "content-type": "application/octet-stream",
            "X-RapidAPI-Key": "cf22b3a36fmsh20b00b7a485c074p15eaa5jsnb923d2ed671f",
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }
        data=requests.get(url="https://irctc1.p.rapidapi.com/api/v1/getTrainSchedule",headers=headers,params={"trainNo":train_no}).json()
        for i in data["data"]["route"]:
            print(i["state_name"])


obj=IRCTC()