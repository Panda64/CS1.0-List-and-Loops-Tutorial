songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[2])

print(songs[1:3])

songs[2] = "Holiday"

songs.extend(["You Should've Known", "Out Of Love", "Opp Block Spinners"])

del songs[4]

animals = ["Cat", "Dog", "Lizard"]

animals.append("Snake")

print(animals[2])

del animals[0]

for i in animals:
    print(i)