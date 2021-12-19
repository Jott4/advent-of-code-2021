# the number of times a depth measurement increases

f = open("01.txt", "r")
sonar = f.read().split("\n")
previous_beep = int(sonar[0])
times_depth_increases = 0

for beep in sonar[1:]:
    beep = int(beep)
    if beep > previous_beep:
        times_depth_increases = times_depth_increases + 1
    previous_beep = beep
    
  
print(times_depth_increases)
  
