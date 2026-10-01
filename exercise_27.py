class Device:
    room = "Lab"
   
    def __init__(self, labaratory):
        self.labaratory = labaratory
       
       
first = Device("D-01")
second = Device("D-02")

Device.room = "Lab 2"
first.room = "Repair Bench"

print(first.room)
print(second.room)
print(Device.room)