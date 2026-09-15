def make_room_code(floor_number, room_number):
    return "FLOOR-" + str(floor_number) + "-ROOM-" + str(room_number)

def main():
    room_code = make_room_code(7, 42)
    print(f"Room code 1: {room_code}")
    print(f"Room code 2: {make_room_code(9, 45)}")
    print(f"Room code 3: {make_room_code(1, 4)}")

if __name__ == "__main__":
    main()