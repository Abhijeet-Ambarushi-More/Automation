import schedule
import time
import datetime

def Display():      # Callback function
    print("Jay Ganesh...",datetime.datetime.now())  # First is module second is class
def main():
    print("Automation screipt started ")     

    schedule.every(1).minute.do(Display)

    # Issue (need to keep process alive)

if __name__ == "__main__":
    main()