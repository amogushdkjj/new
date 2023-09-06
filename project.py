print("You are off on your space mission! You've just taken off and left the Earth's atmosphere. Your team is ready for an adventure of a lifetime! The goal of this mission is to try to find life in the universe. As the captain - you now have an important choice. Where do you go?")
userInput = input("Enter A or B. A) Head towards Mars B) Head into empty space ")

if userInput == 'A':
    print("you were flying towards mars and then suddenly an asteroid is coming towards your space ship?? you can either try to destroy it or attempt flying around it")
    Input = input("A: press the button that should fire a laser at the asteroid, B: tried to steer around it ")
    if Input == 'A':
        print("so you tried to shoot the laser at the asteroid and it missed and hit mars instead. also for some reason the whole planet just exploded. uh oh! I think you wont find life on the planet or on your ship anymore")
    elif Input == 'B':
        print("you just managed to barely get past the asteroid without it hitting your space ship, so you guys got to mars safely. but after looking all over the place, you guys didnt find any signs of life. aw man!")

elif userInput == 'B':
    print("you were flying into the empty space for a while until eventually you see 2 planets, a green planet and an orange planet. which one will you go towards?")
    input2 = input("enter A or B. a: go to the green planet, b: go to the orange planet ")
    if input2 == 'A':
        print("when you were arriving to the green planet you saw that it was filled with forests and plants. you were greeted by space monkeys who happily welcomed you into their home. you guys then had a party with bananas. mission success!")
    elif input2 == 'B':
        print("you go to the orange planet and upon arrival you notice that the entire planet is made out of lava. the temperature: 1000 degrees. Yep it looks like we shouldnt be going there, try a different place")

else: 
     print("You entered something wrong - refresh and try again!")