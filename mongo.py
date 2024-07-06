from pymongo import MongoClient
from bson.objectid import ObjectId

# local mongo
client = MongoClient('mongodb://localhost:27017/')
db = client['cats_db']
collection = db['cats_collection']

def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    collection.insert_one(cat)
    print(f"Cat {name} created.")

def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Cat with name {name} is not found.")

def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count:
        print(f"Cant's age {name} is set to {new_age}.")
    else:
        print(f"Cat with name {name} is not found.")

def add_feature_to_cat(name, feature):
    result = collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.matched_count:
        print(f"Feature '{feature}' added to cat {name}.")
    else:
        print(f"Cat with name {name} is not found.")

def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count:
        print(f"Cat with name {name} deleted.")
    else:
        print(f"Cat with name {name} is not found.")

def delete_all_cats():
    result = collection.delete_many({})
    print(f"All cats are deleted. Record {result.deleted_count} removed.")

if __name__ == "__main__":
    create_cat("bob", 3, ["piss in corner", "allow to pet", "redhead"])
    read_all_cats()
    read_cat_by_name("bob")
    update_cat_age("bob", 4)
    add_feature_to_cat("bob", "like to play")
    read_cat_by_name("bob")
    delete_cat_by_name("bob")
    read_all_cats()
    delete_all_cats()
