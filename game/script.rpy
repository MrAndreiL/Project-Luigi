define michael = Character("Michael")
define noah = Character("Noah")
define mituski = Character("Mitsuki")
define player = Character("Skyler")

label start:
    scene blackk
    pause
    # Insert night-like audio file here.
    "{i}Well… it had to get to this in the end, huh?{/i}"
    "{i}And to think I could have had a serene high school life, but…{/i}"
    # Stop the music.

    pause
    scene playersroom
    # Insert happy music here.
    "{i}…I have to apply for a club!{/i}"
    "..."
    player "But you have to do stuff at a club!"
    "{i}I just want some peace and quiet…{/i}"
    $ y = renpy.input("Well... How should I name my character?")
    "..."
    player "Whatever, I’ll decide tomorrow. I’m too tired for this!"
    player "It’s not like the world will end by then."
    "{i}Wouldn’t be that bad if it did though.{/i}"
    # Stop music.

return 