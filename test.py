def generate_timetable(subjects, teachers, rooms, days, slots):
    timetable = {}
    for day in days:
        timetable[day] = {}
        for slot in slots:
            timetable[day][slot] = None
    
    for subject in subjects:
        for session in range(subject["sessions_per_week"]):
            for day in days:
                for slot in slots:
                    if timetable[day][slot] is None:
                        timetable[day][slot] = {
                            "subject": subject["name"],
                            "teacher": subject["teacher"],
                            "room": rooms.pop(0)  
                        }
                        break
                else:
                    continue
                break
    return timetable
