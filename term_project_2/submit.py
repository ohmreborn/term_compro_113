#------------------------------------------- IMDB HEADER -------------------------------------------
print("หวัดดีน้อง")
# Only 'import json' command is allowed!!!
# Failing to follow this rule, you will get zero mark :_)
import json
print("adssadasd")

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

# specifying the zip file name
filename = "/Users/phongsaphak/Downloads/IMDB_movies_merged.json"

data = read_json(filename)
# print(data[0])
#------------------------------------------- IMDB HEADER -------------------------------------------
def q1():
    ls = []
    for i in range(len(data)):
        try:
            for j in data[i]['cast']:
                    if j['name'] == 'Harrison Ford' and data[i]['director']['name'] != 'Steven Spielberg':
                        x = [data[i]['director']['name'] ,data[i]['ratingValue']]
                        ls.append(x)
            
        except:
            continue

    ls.sort(key=lambda x:x[1] ,reverse=True)
    count = 0
    ls_name = []

    for i in range(len(ls)):
        if ls[i][1] == ls[i-1][1]:
            ls_name.append(ls[i][0])
            count += 0
        else:
            count += 1
            if count > 5:
                break
            ls_name.append(ls[i][0])

    ls_name.sort()
    for name in ls_name:
        print(name)

def q2():
    ls = []
    for i in range(len(data)):
        try:
            ls_name = []
            for j in data[i]['cast']:
                ls_name.append(j['name'])
                if  "Harrison Ford" in ls_name and "Tommy Lee Jones" in ls_name and data[i]['director']['name'] != "George Lucas" and data[i]['director']['name'] != "Steven Spielberg":
                    ls.append(data[i]['name'])

        except:
            continue

    print(ls[0])
