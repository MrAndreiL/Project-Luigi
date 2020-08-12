define michael = Character("Michael")
define noah = Character("Noah")
define mitsue = Character("Mitsue")

image mitsueSmile = "mitsueSmile.png"
image mitsueSmileUpL = "mitsueSmileUpL.png"
image mitsueClosedSmile = "mitsueClosedSmile.png"
image mitsueWinkSmile = "mitsueWinkSmile.png"
image mitsueWorriedTalk = "mitsueWorriedTalk.png"

label start:
    scene blackk
    pause
    # Insert night-like audio file here.
    "{i}Well… it had to get to this in the end, huh?{/i}"
    "{i}And to think I could have had a serene high school life, but…{/i}"
    # Stop the music.
    pause

    scene playersroom with fade 
    # Insert happy music here.
    "{i}…I have to apply for a club!{/i}"
    "..."
    "But you have to do stuff at a club!"
    "{i}I just want some peace and quiet…{/i}"
    $ y = renpy.input("I'll just fill in my name.")
    "..."
    y "Whatever, I’ll decide tomorrow. I’m too tired for this!"
    y "It’s not like the world will end by then."
    y "{i}Wouldn’t be that bad if it did though.{/i}"
    # Stop music.

    scene outsideschool with fade
    y "Ugh..."
    mitsue "Why the long face so early in the morning?"
    "!.."
    show mitsueSmile with fade
    y "Ah, mornin!"
    hide mitsueSmile
    show mitsueSmileUpL
    "And there she is! Our school’s Morning Glory… spreading joy or something."
    "Mitsue’s a little too much for me at times and- oh, ok, walk with me, sure."
    "There it goes, my peaceful morning."
    "Actually, wait. This bubbly blue-head should know some oke-ish clubs."
    "..."
    y "Hey..."
    hide mitsueSmileUpL
    show mitsueSmile
    y "Have you signed up for any clubs?"
    mitsue "Of course!"
    hide mitsueSmile
    show mitsueClosedSmile
    mitsue "I’m in the art club, although I just ignore the tasks they give me"
    hide mitsueClosedSmile
    show mitsueWinkSmile
    y "Oh, ok-"
    mitsue "There’s also the DnD club."
    hide mitsueWinkSmile
    show mitsueSmileUpL
    mitsue "Aki and I came up with it, but we need more members…"
    hide mitsueSmileUpL
    show mitsueWorriedTalk
    "No wait, don’t ask me…"
    pause
return 