
import random

class Character:
    def __init__(self,name="",color="",hat="",num_tasks=0):
        self.name = name
        self.color = color
        self.hat = hat
        self.status = True
        self.tasks = num_tasks
        self.task_list = []
        given_tasks = ['Adjust engine output', 'Calibrate distributor', 'Map course', 'Clear out O2 filter', 'Destroy asteroids',
        'Redirect power', 'Empty garbage', 'Secure wiring', 'Fill engines tanks', 'Inspect laboratory', 'Move shields', 'Steady steering',
        'Initiate reactor', 'Submit personal info', 'Sign in with ID', 'Enable manifolds', 'Sync data']
        x = 16
        for i in range(self.tasks):
            y = random.randint(0,x)
            self.task_list.append(given_tasks[y])
            given_tasks.pop(y)
            x-=1

    def __repr__(self):
        if self.status == True:
            return self.name + ": " + self.color + ", wearing a " + self.hat + " - Health status: Alive"
        else:
            return self.name + ": " + self.color + ", wearing a " + self.hat + " - Health status: Ghost"

    def get_identity(self):
        return "Character"

class Crewperson(Character):
    def __init__(self,name="",color="",hat="",num_tasks=0):
        Character.__init__(self,name,color,hat,num_tasks)

    def complete_task(self):
        if self.task_list == []:
            print(self.name + " has completed all their tasks")
        else:
            print(self.name + " completed the " + self.task_list[0] + " task.")
            self.task_list.pop(0)

    def get_identity(self):
        return "Crewperson"

class Pretender(Character):
    def __init__(self,name="",color="",hat="",num_tasks=0):
        Character.__init__(self,name,color,hat,num_tasks)

    def eliminate(self,target):
        print(self.name + " eliminated " + target.name)
        target.status = False

    def get_identity(self):
        return "Pretender"

class Game:
    def __init__(self,player_list):
        self.player_list = player_list

    def check_winner(self):
        a = 0
        crewlist = []
        pretenders = []
        for player in self.player_list:
            if player.get_identity() == "Crewperson":
                crewlist.append(player)
            else:
                pretenders.append(player)
        z = 0
        c = 0
        for crew in crewlist:
            if crew.task_list == []:
                z+=1
            if crew.status == True:
                c+=1
        if z == len(crewlist):
            a = 1
        b = 0
        for pretender in pretenders:
            if pretender.status == False:
                b+=1
        if b == len(pretenders):
            a = 1
        if len(pretenders) - b >= c:
            a = 2
        if a == 1:
            print("Crewpersons win!")
            return "C"
        elif a == 2:
            print("Pretenders win!")
            return "P"
        else:
            return "-"

    def meeting(self):
        d = random.randint(0,len(self.player_list)-1)
        for player in self.player_list:
            print(player.name + " voted for " + str(self.player_list[d].name) + ".")
        print(str(self.player_list[d].name) + " was eliminated.")
        return str(self.player_list[d].name)

    def play_game(self):
        crewlist = []
        pretenders = []
        for player in self.player_list:
            if player.get_identity() == "Crewperson":
                crewlist.append(player)
            else:
                pretenders.append(player)
        n = 0
        while n!=1:
            for crew in crewlist:
                r = random.randint(1,3)
                for j in range(r):
                    crew.complete_task()
            for pretender in pretenders:
                if pretender.status == True:
                    s = random.randint(0,len(crewlist)-1)
                    if crewlist[s].status == True:
                        print(str(pretender.name) + " eliminated " + str(crewlist[s].name) + ".")
                        crewlist[s].status = False
            if self.check_winner() == "-":
                self.meeting()
                if self.check_winner() != "-":
                    n+=1
            else:
                n+=1
        return self.check_winner()
