import json
from sqlalcemy import *
import datetime

DATABASEURI = "postgresql://cs3731:abc123@104.196.18.7/w4111"
db = create_engine(DATABASEURI)
db.echo = False # No logging
metadata = MetaData(db)

users = Table('Users', metadata, autoload = True)
community = Table('Community', metadata, autoload = True)
admin = Table('Admin', metadata, autoload = True)
interest = Table('Interest', metadata, autoload = True)
post = Table('Post', metadata, autoload = True)
likes = Table('Likes', metadata, autoload = True)
reply = Table('Reply', metadata, autoload = True)
subreply = Table('Subreply', metadata, autoload = True)


# return the dict form of attribute and value of one-line sql result
def row2dict(row):
    if row is None:
        return None
    d = {}
    for rs in row.keys():
        d[rs] = row[rs]
    return d


# return the list form of attribute and value of multi=-lines sql results.
# each result in one dict
def multirow2listdict(row):
    if row is None:
        return None
    list = []
    for rs in row:
        dict = {}
        for key in rs.keys():
            dict[key] = rs[key]
        list.append(dict)
    return list