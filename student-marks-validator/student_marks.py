subjects = {
    "English" : 0,
    "math"    : 0,
    "science" : 0,
    "biology" : 0,
    "physics" : 0
}
class InvlidMarkError(Exception):
    pass
total = 0
for name,score in subjects.items():
    try:
        score = int(input(f"enter a {name} number"))
        total+=score
        subjects[name]=score
        # print(subjects)
        for name,score in subjects.items():
            if  score < 0 or score > 100:
                raise InvlidMarkError("Enter number between 0 to 100")
    except InvlidMarkError:
       print(f"{name} is  invalid marks")
       number = int(input("enter agian"))
       subjects[name]=number
       print(f"{name} is {number}")
    #    print(subjects)
    except ValueError:
        print("Please Enter only numeber")
avg = total/len(subjects)
print(subjects)
if avg >= 90:
    print(f"avg {avg} Grade A")
elif avg >= 80:
    print(f"avg {avg} Grade B")
elif avg>=70:
    print(f"avg is {avg} Grade C")
elif avg >= 50:
    print(f"avg is {avg} Grade D")
else:
    print("your fail")
