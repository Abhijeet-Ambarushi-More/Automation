import schedule
import time
import datetime

def Display():      # Callback function
    print("Jay Ganesh...",datetime.datetime.now())  # First is module second is class
def main():
    print("Automation screipt started ")     

    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)   # 1-1 second zopel main thread

    print("end of automation script")

if __name__ == "__main__":
    main()