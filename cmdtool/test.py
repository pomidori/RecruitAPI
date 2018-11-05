import pyhdb


connection = pyhdb.connect(
    host='35.241.77.219',
    port=39013,
    user='SYSTEM',
    password='Welcome1')

cursor = connection.cursor()
print("successfully connected")

# current_dir = os.getcwd()
# dir = current_dir + "/data_0.csv"

cursor.execute(
    'CREATE TABLE TEST2("NAMES" VARCHAR (255) null)'
)

cursor.execute("INSERT INTO TEST2 VALUES('Hello Python World')")
print("successfully inserted")

#
# cursor.execute(
# r"IMPORT FROM CSV FILE '/Users/i318656/Documents/Programming/Python/RecruitAPI/data_0.csv' \
# INTO ML_DATA.MYTABLE_IMPORTSQL \
# WITH \
#    RECORD DELIMITED BY '\n' \
#    FIELD DELIMITED BY ',' \
#    OPTIONALLY ENCLOSED BY '"' \
#    SKIP FIRST 1 ROW　\
#    FAIL ON INVALID DATA　\
#    ERROR LOG '/Users/i318656/Documents/Programming/Python/RecruitAPI/data_0.csv.err'")
