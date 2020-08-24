define michael = Character("Michael")
define noah = Character("Noah")
define mitsue = Character("Mitsue")
define aki = Character("Aki")

# Mitsue
image mitsueSmile = "mitsueSmile.png"
image mitsueSmileUpL = "mitsueSmileUpL.png"
image mitsueClosedSmile = "mitsueClosedSmile.png"
image mitsueSurprisedTalk = "mitsueSurprisedTalk.png"
image mitsueWinkSmile = "mitsueWinkSmile.png"
image mitsueWorriedTalk = "mitsueWorriedTalk.png"
image mitsueTalkUpL = "mitsueTalkUpL.png"

# Michael
image michaelNormal = "michaelNormal.png"
image michaelQuiestioningSideL = "michaelQuiestioningSideL.png"
image michaelQuiestioningTalkFronL = "michaelQuiestioningTalkFronL.png"
image michaelSmile1 = "michaelSmile1.png"
image michaelSurprised = "michaelSurprised.png"
image michaelTalkSideL = "michaelTalkSideL.png"
image michaelWorriedSideL = "michaelWorriedSideL.png"

# Aki
image akiNormal = "akiNormal.png"
image akiSmile = "akiSmile.png"
image akiTalk = "akiTalk.png"

# Noah
image noahConfidentTalk = "noahConfidentTalk.png"
image noahSmile = "noahSmile.png"
image noahSurprised = "noahSurprised.png"
image noahTalk = "noahTalk.png"
image noahWorriedSmile = "noahWorriedSmile.png"
image noahWorriedTalk = "noahWorriedTalk.png"
image noahWorriedTalk2 = "noahWorriedTalk2.png"


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
    mitsue "Why don't you join our club?"
    hide mitsueWorriedTalk
    show mitsueWinkSmile
    "{i}I wasn’t thinking about a you-directed club but ok--{/i}"
    y "Sure... I'll drop by later"
    mitsue "Awesome-possum! We meet up after school."
    hide mitsueWinkSmile
    show mitsueClosedSmile
    y "Ok, well… I gotta go that way. See you later."
    mitsue "Bye-bye!"
    hide mitsueClosedSmile
    show mitsueWinkSmile
    hide mitsueWinkSmile

    # Hallway
    scene hallway with fade
    "{i}I acted like I knew what DnD is but...{/i}"
    "{i}Actually, I can search it up"
    "..."
    "{i}What do you mean a fantasy role-playing game?!{/i}"
    "{i}Should I...dress up?{/i}"
    "{i}No, no. That would be ridiculous.{/i}"
    "{i}I'm sure they're just playing a board-game or something like that{/i}"
    "..."
    "{i}Or at least I HOPE SO{/i}"
    y "...!"
    y "Hey, Michael."
    show michaelNormal with fade
    michael "Morning"
    hide michaelNormal
    show michaelSmile1
    pause 
    hide michaelSmile1
    show michaelQuiestioningSideL
    michael "You look gloomier than usual."
    hide michaelQuiestioningSideL
    show michaelQuiestioningTalkFronL
    y "Oh, you know."
    hide michaelQuiestioningTalkFronL
    show michaelNormal
    y "I bumped into Mitsue on the way here."
    michael "Figured" 
    hide michaelNormal
    show michaelSmile1
    michael "Heard she has a club, I’ll go later to see what’s up."
    michael "Dehnam told me to sign up for one anyways."
    hide michaelNormal
    show michaelWorriedSideL
    y "He got you too?!"
    hide michaelWorriedSideL
    show michaelSurprised
    michael "Yeah, well… that’s just how he is."
    hide michaelSurprised
    show michaelSmile1
    michael "Let’s go together later."
    y "Sounds good! See ya."
    hide michaelSmile1
    "{i}Man! Michael is so cool.{/i}"
    "{i}Oh, well. I’ll just ask him later I guess—{/i}"

    # Hallway part 2, Shake
    scene hallway with hpunch
    y "Oops, sorry!"
    noah "!!"
    show noahSurprised with fade
    noah "It's ok."
    hide noahSurprised
    show noahSmile
    y "Oh...ok."
    "..."
    noah "See ya!"
    hide noahSmile
    show noahTalk
    y "Uh, bye?"
    hide noahTalk
    "{i}Heck! You couldn’t have been more awkward!{/i}"
    "{i}That guy! He’s always so nice, but seems so unapproachable!{/i}"
    "{i}Would be nice if we became friends, but…{/i}"
    "{i}…I saw him hanging out with the guys from the baseball club.{/i}"
    "{i}Yep, no way we got things in common so I should just leave it.{/i}"
    "{i}Class is about to start, let’s focus on that.{/i}"
    scene blackk with fade
    "..."

    # Classroom.
    scene classroomday with fade
    y "Ugh..."
    "{i}What a long day… and there’s still more.{/i}"
    y "I just wanna go sleep."
    michael "No time for sleep, come on."
    michael "It's gonna be fun."
    show michaelSmile1
    y "If you say so"
    y "Let’s just go before I change my mind."
    michael "Sure."
    
    scene classroomday with fade
    michael "I think it's here"
    hide michaelSmile1
    show michaelQuiestioningSideL
    hide michaelQuiestioningSideL
    mitsue "You guys actually came!"
    show mitsueSurprisedTalk
    mitsue "Now we just have to wait a little."
    hide mitsueSurprisedTalk
    show mitsueWinkSmile
    mitsue "“I managed to convince a third person to check our club out hehehe..."
    hide mitsueWinkSmile
    show mitsueClosedSmile
    y "Who fell for this?"
    hide mitsueClosedSmile
    show mitsueSmile 
    y "Who fell for this?"
    hide mitsueSmile
    show noahWorriedTalk at center
    show mitsueSmile at left
    noah "Sorry if I'm late."
    hide noahWorriedTalk
    show noahWorriedTalk2 at center
    noah "Did I miss anything?" 
    show michaelTalkSideL at right
    michael "I guess this guy did."
    pause
return 










