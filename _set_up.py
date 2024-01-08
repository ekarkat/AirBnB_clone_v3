#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                    "root",
                                    "root",
                                    "localhost",
                                    "hbnb_dev_db"),
                                pool_pre_ping=True)

# Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)

session = Session()



# states_list = [
#     [{"name": "California"}, {"cities": ["Los Angeles", "San Francisco", "San Diego"]}],
#     [{"name": "New York"}, {"cities": ["New York City", "Buffalo", "Rochester"]}],
#     [{"name": "Texas"}, {"cities": ["Houston", "Dallas", "Austin"]}],
#     [{"name": "Florida"}, {"cities": ["Miami", "Orlando", "Tampa"]}],
#     [{"name": "Illinois"}, {"cities": ["Chicago", "Springfield", "Peoria"]}],
#     [{"name": "Ohio"}, {"cities": ["Columbus", "Cleveland", "Cincinnati"]}],
#     [{"name": "Georgia"}, {"cities": ["Atlanta", "Savannah", "Athens"]}],
#     [{"name": "Colorado"}, {"cities": ["Denver", "Colorado Springs", "Boulder"]}]
# ]

# for state in states_list:
#     state_obj = State(name=state[0]["name"])
#     session.add(state_obj)
#     session.commit()
#     print(state[0]["name"] + "has been added to database")

#     for city_name in state[1]["cities"]:
#         city_obj = City(name=city_name, state_id=state_obj.id)
#         session.add(city_obj)
#         session.commit()
#         print("city {} has been added".format(city_name))

result = session.query(State).all()

print(result[0].id)
