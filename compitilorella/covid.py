import threading
from threading import Lock
import sys

sys.stdout = open('output.txt', 'w')

class threadCovid(threading.Thread):

    lock_ = threading.Lock()
    tot_deaths = 74159
    tot_infected = 2107166
    tot_healed = 1463111

    def __init__(self, file, list = []) -> None:
        threading.Thread.__init__(self)
        self.file = file
        self.list = []

    def covid_stats(self):
        file_to_open = "covid_data_" + str(self.file) + "_2021.csv"
        with open(str(file_to_open)) as csvfile:
            for line in csvfile:
                line = line.strip()
                line = line.split(",")
                self.list.append(line)

        print(self.list)
        for row in range(1, len(self.list)):
            with threadCovid.lock_:
                threadCovid.tot_deaths += int(self.list[row][1])
                threadCovid.tot_healed += int(self.list[row][2])
                threadCovid.tot_infected += int(self.list[row][3])

    def __repr__(self) -> str:
        print(threadCovid.tot_deaths, threadCovid.tot_healed, threadCovid.tot_infected)
        
if __name__ == "__main__":
    list_months = ["jan", "feb", "mar","apr"]
    for i in range(4):
        t = threadCovid(list_months[i])
        t.covid_stats()

    t.__repr__()