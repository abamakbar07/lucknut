# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ev")

screen coba():
    imagemap:
        ground "image3neo.png" at center
        hotspot (48, 85, 108, 92) action Jump ("teteKiri")
        hotspot (162, 89, 112, 87) action Jump ("teteKanan")

screen lagi():
    imagemap:
        ground "image1neo.png" at center
        text "mau maen tete lagi?"
        call coba

# The game starts here.

label start:

    show bg

    show image1neo
    e "Hello world"
    e "Mau maen tete dengan ku?"
    hide image1neo

    call screen coba

# label 

label teteKiri:

    e "tete kiri ini melambangkan kesetiaan"

    call screen lagi

label teteKanan:

    e "tete kanan emang lebih besar, unch"

    call screen lagi
    return
