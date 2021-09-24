import sqlite3 as sl

con = sl.connect('lifeApp.db')

with con:
    currDate0 = con.execute("select date('now', 'localtime')")
    for value in currDate0:
        currDate = value[0]

    currTime0 = con.execute("select time('now', 'localtime')")
    for value in currTime0:
        currTime = value[0]

    con.execute(f"insert into life_app_main(date, time) values('{currDate}', '{currTime}');")

    currId0 = con.execute("select last_insert_rowid()")
    for value in currId0:
        currId = value[0]
        # print(currId)

    countAllGoals0 = con.execute(f"select count(*) from life_app_main where date='{currDate}' and all_goal='y';")
    for value in countAllGoals0:
        countAllGoals = value[0]

    countWorkoutYoga0 = con.execute(f"select count(*) from life_app_main where date='{currDate}' and workout_yoga='y';")
    for value in countWorkoutYoga0:
        countWorkoutYoga = value[0]

    countRwd0 = con.execute(f"select count(*) from life_app_main where date='{currDate}' and rwd='y';")
    for value in countRwd0:
        countRwd = value[0]

    countHardware0 = con.execute(f"select count(*) from life_app_main where date='{currDate}' and hardware='y';")
    for value in countHardware0:
        countHardware = value[0]

    countSoftware0 = con.execute(f"select count(*) from life_app_main where date='{currDate}' and software='y';")
    for value in countSoftware0:
        countSoftware = value[0]

    countVeggies0 = con.execute(f"select count(*) from life_app_main where date='{currDate}' and veggies='y';")
    for value in countVeggies0:
        countVeggies = value[0]

    if countVeggies != 0 and countSoftware != 0 and countRwd != 0 and countHardware != 0 and countWorkoutYoga != 0:
        con.execute(f"update life_app_main set all_goal='y' where id={currId};")

    workoutYoga0 = con.execute(f"select workout_yoga from life_app_main where id={currId}")
    for value in workoutYoga0:
        workoutYoga = value[0]

    rwd0 = con.execute(f"select rwd from life_app_main where id={currId}")
    for value in rwd0:
        rwd = value[0]

    hardware0 = con.execute(f"select hardware from life_app_main where id={currId}")
    for value in hardware0:
        hardware = value[0]

    software0 = con.execute(f"select software from life_app_main where id={currId}")
    for value in software0:
        software = value[0]

    veggies0 = con.execute(f"select veggies from life_app_main where id={currId}")
    for value in veggies0:
        veggies = value[0]

    allGoals0 = con.execute(f"select all_goal from life_app_main where id={currId}")
    for value in allGoals0:
        allGoals = value[0]

    mood = input("how do you feel? ")
    con.execute(f"update life_app_main set mood='{mood}' where id={currId}")

    recAct = input("most recent activity: ")
    con.execute(f"update life_app_main set recent_activity='{recAct}' where id={currId}")


    if countWorkoutYoga == 0:
        workoutYoga = input("work out/yoga: ")
        con.execute(f"update life_app_main set workout_yoga='{workoutYoga}' where id={currId}")
    else:
        con.execute(f"update life_app_main set workout_yoga='y' where id={currId}")

    if countRwd == 0:
        rwd = input("read/write/draw: ")
        con.execute(f"update life_app_main set rwd='{rwd}' where id={currId}")
    else:
        con.execute(f"update life_app_main set rwd='y' where id={currId}")

    if countHardware == 0:
        hardware = input("hardware: ")
        con.execute(f"update life_app_main set hardware='{hardware}' where id={currId}")
    else:
        con.execute(f"update life_app_main set hardware='y' where id={currId}")

    if countSoftware == 0:
        software = input("software: ")
        con.execute(f"update life_app_main set software='{software}' where id={currId}")
    else:
        con.execute(f"update life_app_main set software='y' where id={currId}")

    if countVeggies == 0:
        veggies = input("veggies: ")
        con.execute(f"update life_app_main set veggies='{veggies}' where id={currId}")
    else:
        con.execute(f"update life_app_main set veggies='y' where id={currId}")

    if workoutYoga == 'y' and rwd == 'y' and hardware == 'y' and software == 'y' and veggies == 'y':
        con.execute(f"update life_app_main set all_goal='y' where id={currId}")

    else:
        con.execute(f"update life_app_main set all_goal='n' where id={currId};")


    nexAct = input("next activity: ")
    con.execute(f"update life_app_main set next_activity='{nexAct}' where id={currId}")

    data = con.execute("select * from life_app_main;")
    for row in data:
        print(row)
