class Room:
    building = 'Ky Tuc Xa TVU'
    count = 0
    def __init__(self, room_no, capacity = 0):
        self.room_no = room_no
        self.capacity = capacity
        self.occupants = []
    
    def is_full(self):
        if Room.count >= self.capacity:
            return True

    def check_in(self, name):
        if Room.count >= self.capacity:
            raise ValueError(f'Room {self.room_no} is Full')
        
        else:
            if name in self.occupants:
                raise ValueError(f'{name} already in room')
            self.occupants.append(name)
            Room.count += 1

    def check_out(self, name):
        if name in self.occupants:
            self.occupants.remove(name)
            Room.count -= 1
            return True
        return False

    def __str__(self):
        string = ", ".join(self.occupants)
        return f'{self.room_no} [{Room.count}/{self.capacity}]: {string}'
            
            
if __name__ == "__main__":
    r = Room("A101", 2)
    r.check_in("An"); r.check_in("Binh")
    print(r)
    print(r.is_full(), Room.building)
    try:
        r.check_in("Chi")
    except ValueError as e:
        print("Error:", e)
    print(r.check_out("An"), r.check_out("Dung"))
    print(r)


        

