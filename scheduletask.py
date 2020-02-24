import json
from datetime import datetime, timedelta
import copy


def schedule(new_profile,startdate,enddate,user):
    userdata = {}
    date_list = []

    with open('schedule.json', 'r') as f:
        data = json.load(f)

    user1 = {}
    list_user = []
    remove_list = []

    user1["profile"] = new_profile
    user1["startDate"] = startdate
    user1["endDate"] = enddate
    check_user = user
    date_format = "%d-%m-%Y"
    new_startDate = datetime.strptime(startdate, date_format)
    new_endDate = datetime.strptime(enddate, date_format)


    if new_startDate <= new_endDate:

        if check_user not in data.keys():
          list_user.append(user1)
          data.update({check_user : list_user})
          with open('schedule.json', 'w') as json_file:
              json.dump(data, json_file, indent=4)
              print("User Inserted Successfully")

        else:
            ctr = -1
            temp = copy.deepcopy(data[check_user])
            print(temp)
            for i in data[check_user]:
                ctr += 1
                print(i)
                date_format = "%d-%m-%Y"
                new_startdate = datetime.strptime(startdate, date_format)
                new_enddate = datetime.strptime(enddate, date_format)
                profile = i["profile"]
                sd = i["startDate"]
                ed = i["endDate"]
                ed = datetime.strptime(ed, date_format)
                sd = datetime.strptime(sd, date_format)

                # Case: 1
                if sd < new_startdate and ed > new_startdate and ed < new_enddate and sd < new_enddate:
                    print("Overlap 1")

                    if profile != new_profile:
                        delta = ed - new_startdate
                        new_startdate = ed - timedelta(days=delta.days + 1)
                        new_startdate = new_startdate.strftime("%d-%m-%Y")
                        temp[ctr]["endDate"] = new_startdate
                    else:
                        print("Same Profile 1")
                        sd = sd.strftime(("%d-%m-%Y"))
                        user1["startDate"] = sd
                        if i["profile"] == profile:
                            temp.remove(i)
                            ctr -= 1
                            # remove_list.append(i)
                # Case: 2
                elif sd > new_startdate and sd < new_enddate and ed > new_startdate and ed > new_enddate:
                    print("Overlap 2")

                    if profile != new_profile:
                        edit_date = new_enddate + timedelta(days=1)
                        edit_date = edit_date.strftime("%d-%m-%Y")
                        print(edit_date)
                        temp[ctr]["startDate"] = edit_date
                    else:
                        print("Same Profile 2")
                        ed = ed.strftime(("%d-%m-%Y"))
                        user1["endDate"] = ed
                        if i["profile"] == profile:
                            temp.remove(i)
                            ctr -= 1


                # Case : 3
                elif sd == new_startdate and sd < new_enddate and ed > new_startdate and ed < new_enddate:
                    print("Overlap 3 ")

                    if profile != new_profile:
                        if i["profile"] == profile:
                            temp.remove(i)
                            ctr -= 1

                    else:
                        sd = sd.strftime(("%d-%m-%Y"))
                        user1["startDate"] = sd
                        if i["profile"] == profile:
                            temp.remove(i)
                            ctr -= 1


                # Case : 4
                elif sd < new_startdate and sd < new_enddate and ed > new_startdate and ed > new_enddate:
                    print("Overlap 4")

                    if profile != new_profile:
                        new_userprofile = {}
                        edit_date1 = new_startdate - timedelta(days=1)
                        edit_date1 = edit_date1.strftime("%d-%m-%Y")
                        temp[ctr]["endDate"] = edit_date1

                        edit_date2 = new_enddate + timedelta(days=1)
                        edit_date2 = edit_date2.strftime("%d-%m-%Y")
                        edit_date3 = ed
                        edit_date3 = edit_date3.strftime("%d-%m-%Y")
                        new_userprofile["profile"] = profile
                        new_userprofile["startDate"] = edit_date2
                        new_userprofile["endDate"] = edit_date3
                        data[check_user].append(new_userprofile)
                    else:
                        new_startdate = sd
                        new_startdate = new_startdate.strftime(("%d-%m-%Y"))
                        user1["startDate"] = new_startdate
                        new_enddate = ed
                        new_enddate = new_enddate.strftime(("%d-%m-%Y"))
                        user1["endDate"] = new_enddate
                        if i["profile"] == profile:
                            temp.remove(i)
                            ctr -= 1


                # Case : 5
                elif sd < new_startdate and ed == new_startdate and ed < new_enddate and sd < new_enddate:
                    print("Overlap 5")
                    if profile != new_profile:
                        delta = ed - new_startdate
                        new_startdate = ed - timedelta(days=delta.days + 1)
                        new_startdate = new_startdate.strftime("%d-%m-%Y")
                        temp[ctr]["endDate"] = new_startdate
                    else:
                        new_startdate = sd
                        sd = sd.strftime(("%d-%m-%Y"))
                        user1["startDate"] = sd
                        if i["profile"] == profile:
                            temp.remove(i)
                            ctr -= 1



                # Case : 6
                elif sd > new_startdate and ed > new_startdate and ed < new_enddate and sd < new_enddate:
                    print("Overlap 6")
                    if i["profile"] == profile:
                        temp.remove(i)
                        ctr -= 1

                # Case : 7
                elif sd == new_startdate and ed > new_startdate and ed > new_enddate and sd < new_enddate:
                    print("Overlap 7")

                    if profile != new_profile:
                        sd = new_enddate + timedelta(days=1)
                        sd = sd.strftime("%d-%m-%Y")
                        temp[ctr]["startDate"] = sd
                    else:
                        new_enddate = ed
                        ed = ed.strftime(("%d-%m-%Y"))
                        user1["endDate"] = ed
                        if i["profile"] == profile:
                            temp.remove(i)
                            ctr -= 1


                # Case : 8
                elif sd > new_startdate and ed > new_startdate and ed == new_enddate and sd < new_enddate:
                    print("Overlap 8")
                    if i["profile"] == profile:
                        temp.remove(i)
                        ctr -= 1


                # Case : 9
                elif sd > new_startdate and ed > new_startdate and ed > new_enddate and sd == new_enddate:
                    print("Overlap 9")

                    if profile != new_profile:
                        sd = new_enddate + timedelta(days=1)
                        sd = sd.strftime("%d-%m-%Y")
                        temp[ctr]["startDate"] = sd
                    else:
                        new_enddate = ed
                        ed = ed.strftime(("%d-%m-%Y"))
                        user1["endDate"] = ed
                        if i["profile"] == profile:
                            temp.remove(i)
                            ctr -= 1


                # Case : 10
                elif sd == new_startdate and ed > new_startdate and ed == new_enddate and sd < new_enddate:
                    print("Overlap 10")
                    if i["profile"] == profile:
                        temp.remove(i)
                        ctr -= 1


                # Case : 11
                elif sd < new_startdate and ed > new_startdate and ed == new_enddate and sd < new_enddate:
                    print("Overlap 11")

                    if profile != new_profile:
                        ed = new_startdate - timedelta(days=1)
                        ed = ed.strftime("%d-%m-%Y")
                        temp[ctr]["endDate"] = ed
                    else:
                        print("Same Profile 11")
                        new_startdate = sd
                        sd = sd.strftime(("%d-%m-%Y"))
                        user1["startDate"] = sd
                        if i["profile"] == profile:
                            temp.remove(i)
                            ctr -= 1


                elif sd == new_startdate and ed == new_startdate and ed < new_enddate and sd < new_enddate:
                    print("Overlap 12")
                    temp.remove(i)
                    ctr -= 1


                elif sd == new_startdate and ed > new_startdate and ed > new_enddate and sd == new_enddate:
                    print("Overlap 13")
                    if profile != new_profile:
                        sd = new_enddate + timedelta(days=1)
                        sd = sd.strftime("%d-%m-%Y")
                        temp[ctr]["startDate"] = sd
                    else:
                        ed = ed.strftime("%d-%m-%Y")
                        user1["endDate"] = ed
                        temp.remove(i)
                        ctr -= 1


                elif sd < new_startdate and ed == new_startdate and ed == new_enddate and sd < new_enddate:
                    print("Overlap 14")
                    if profile != new_profile:
                        sd = new_startdate - timedelta(days=1)
                        sd = sd.strftime("%d-%m-%Y")
                        temp[ctr]["endDate"] = sd
                    else:
                        ed = ed.strftime("%d-%m-%Y")
                        user1["startDate"] = ed
                        temp.remove(i)
                        ctr -= 1


                elif sd == new_startdate == ed == new_enddate:
                    print("Overlap 15")
                    temp.remove(i)
                    ctr -= 1


                elif new_enddate < sd:
                    print("Exception")
                    break

                else:
                    print("No Overlap")

            temp.append(user1)
            data[check_user] = temp[:]

            print("File Write")
            with open('schedule.json', 'w') as json_file:
                temp.sort(key=lambda temp: datetime.strptime(temp["startDate"], "%d-%m-%Y"))
                data[check_user] = temp[:]
                json.dump(data, json_file, indent=4)
                print("User Inserted Successfully")
        return data[check_user]

    else:
        print("Inavlid Dates")


def all_user():
    with open('schedule.json', 'r') as f:
        data = json.load(f)
        return data