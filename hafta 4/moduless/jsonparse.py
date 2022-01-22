from json import load
from moduless.users_data import User_Datas
from geopy.geocoders import Nominatim
import re

loc_long=loc_lat=name_surmane=''
birthdays = list()


def findlocation(x,y):
    geolocator = Nominatim(user_agent="location-finder")
    location = geolocator.reverse(f"{x},{y}")
    country = location.address
    return country

def birthday_parser(birthday):
    pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
    match = pattern.search(birthday)
    birthdays.append(match.group(1))
    birthdays.append(match.group(2))
    birthdays.append(match.group(3))

def email_match_check(email,name):
        pattern =  re.compile(r"([a-zA-Z]+)[\.-_]*([a-zA-Z]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
        match = pattern.search(email)
        email_name = match.group(1)
        email_surname = match.group(2)
        pattern2 =  re.compile(r"([a-zA-Z]+)[' ']([a-zA-Z]+)")
        match2 = pattern2.search(name)
        json_name = match2.group(1)
        json_surname = match2.group(2)
        if  json_name in email_name :
            return 1
        elif  json_surname in email_surname :
            return 1
        else:
            return 0

def username_macth_check(username,json_username):
        pattern = re.compile(r"[A-Za-z]+")
        match = pattern.search(username)
        name = match.group()
        if name in json_username:
            return 1
        else:
            return 0

class JsonParse:

    def __init__(self):
        self.json_data=list()

    def read_json(self,json_path):
        with open(json_path) as json_file:
            json_data=load(json_file)
            for item in json_data:
                datas = User_Datas()

                datas.email=item['email']
                datas.username=item['username']
                name_surname=item['profile']['name']
                datas.emailuserlk = email_match_check(datas.email,name_surname)
                datas.usernamelk = username_macth_check(datas.username,name_surname)
                # bu kısımda doğum günü  ayı ve yılını alıyoruz
                birthday_parser(item["profile"]["dob"])
                datas.birth_year = birthdays.pop()
                datas.birth_month= birthdays.pop()
                datas.birth_day= birthdays.pop()
                

                # üçüncül bir kütüphane kullanarak location bilgisini elde ettik 
                loc_lat=item['profile']['location']['lat']
                loc_long=item['profile']['location']['long']
                datas.country = findlocation(loc_lat,loc_long)
                
            json_file.close()      
        return (self.json_data)   

