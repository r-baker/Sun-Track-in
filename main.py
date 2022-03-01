from datetime import datetime
from Timed_Position import time_pos
import time

"""
track_the_sun() main code to get input on sun location and send motor control
INPUT: none
DO: each minute, will check time to see if it use preset sun position(15min) or sensor ajustment(1min)
RETURN: none
"""
def track_the_sun():
    while True:
        today_now = datetime.now()
        print("now =", today_now)  # to be remove in final code
        # %Y=years %m= month %d= day %H= hours %M= minute %S= seconde
        hours_now = int(today_now.strftime("%H"))  # switch hours from string to integer
        print("L'heure la: ", hours_now)  # to be remove in final code
        minute_now = int(today_now.strftime("%M"))
        time_to_check = hours_now * 100 + minute_now
        print("combinaison heure et minute: ", time_to_check)  # to be remove in final code or front end, TBD

        if minute_now == 00 or minute_now % 15 == 0: # ajout futur d'une sleep pour les heure de la nuit.
            x = int(time_to_check)
            pos_x, pos_z = time_pos(x)
            print(pos_x, " ", pos_z)
            # code toward motor to be add here!
        time.sleep(60)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    track_the_sun()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
