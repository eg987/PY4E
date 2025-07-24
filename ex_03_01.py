sh=input("Enter Hours: ")
sr=input("Enter Rate: ")
fr = float(sr)
fh = float(sh)
# print(fh, fr)
if fh > 40 : 
   # print("Overtime")
    reg = fr * fh
    otp = (fh-40.0) * (fr * 0.5)
   # print (reg, otp)
    xp = reg + otp
else :
    #print("Regular")
    xp= fh * fr
print("Pay:",xp)