from moduless.database import Database
from moduless.jsonparse import JsonParse

def main(__file = None , db = None):
    if(__file != None and db != None):
        json = JsonParse()
        database = Database(db)
        user_list = json.read_json(__file)
        database.create_table()
        for user_data in user_list:
            database.insert_data(user_data)
    else:
        print("Kral bi aksilik var galiba girdiğin pathleri kontrol et :')")


if __name__ == "__main__":
    __file = "ödevler\hafta 4\dataregex.json"
    db = "ödevler\hafta 4\dataregex.db"
    main(__file,db)