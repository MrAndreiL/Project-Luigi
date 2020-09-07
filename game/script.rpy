define michael = Character("Michael")
define noah = Character("Noah")
define mitsue = Character("Mitsue")
define aki = Character("Aki")
define all = Character("All")

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

# Races
$ human = False
$ elf = False
$ dwarf = False
$ goblin = False
$ dragonborn = False
$ tabaxi = False
$ raceString = ""

# Classes.
$ barbarian = False
$ fighter = False
$ monk = False
$ ranger = False
$ paladin = False
$ bard = False
$ classString = ""

label dndExplain:
    show mitsueTalkUpL
    mitsue "So! Dnd stands for Dungeon and Drangons,"
    mitsue "which is an open-ended role-playing game."
    mitsue "That means anything is possible within the game’s rules."
    hide mitsueTalkUpL
    show mitsueWinkSmile
    mitsue "For that, though, everybody will have to create their own character."
    hide mitsueWinkSmile
    show mitsueSmile
    mitsue "It’s quite simple, and Aki and I will help you with the difficult parts, such as abilities, spells etc, etc."
    hide mitsueSmile
    show mitsueTalkUpL
    mitsue "Aki will guide us through the story,"
    hide mitsueTalkUpL
    show mitsueSmile
    mitsue "because there’s also a story,"
    hide mitsueSmile
    show mitsueTalkUpL
    mitsue "so she’ll be our DM, as I said before."
    hide mitsueTalkUpL
    show mitsueSmile
    mitsue "Oh, that stands for Dungeon Master."
    mitsue "Was there anything else?"
    hide mitsueSmile
    show mitsueWorriedTalk
    y "I think I got it!"
    mitsue "Awesome-possum!"
    hide mitsueWorriedTalk
    menu:
        mitsue "But are you sure I shouldn’t explain again?"
        "Actually, tell me again.":
            jump dndExplain
        "No, I’m fine!":
            jump endExplain

label start:
    scene blackk
    pause
    # Insert night-like audio file here.
    "{i}Well… it had to get to this in the end, huh?{/i}"
    "{i}And to think I could have had a serene high school life, but…{/i}"
    # Stop the music.

    scene playersroom with fade 
    # Insert happy music here.
    "{i}…I have to apply for a club!{/i}"
    "..."
    "But you have to do stuff at a club!"
    "{i}I just want some peace and quiet…{/i}"
    $ y = renpy.input("I'll just fill in my name.")
    while y == "":
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
    michael "Morning!"
    hide michaelNormal
    show michaelQuiestioningSideL
    michael "You look gloomier than usual..."
    hide michaelQuiestioningSideL
    show michaelQuiestioningTalkFronL
    y "Oh, you know..."
    hide michaelQuiestioningTalkFronL
    show michaelNormal
    y "I bumped into Mitsue on the way here."
    michael "Figured..." 
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
    show michaelSmile1
    michael "No time for sleep, come on."
    michael "It's gonna be fun."
    y "If you say so"
    y "Let’s just go before I change my mind."
    michael "Sure."
    hide michaelSmile1
    
    scene classroomday with fade
    show michaelQuiestioningSideL
    michael "I think it's here"
    hide michaelQuiestioningSideL
    show mitsueSurprisedTalk
    mitsue "You guys actually came!"
    mitsue "Now we just have to wait a little."
    hide mitsueSurprisedTalk
    show mitsueWinkSmile
    mitsue "I managed to convince a third person to check our club out hehehe..."
    hide mitsueWinkSmile
    show mitsueSmile 
    y "Who fell for this?"
    hide mitsueSmile
    show noahWorriedTalk
    noah "Sorry If I'm late..."
    noah "Have I missed anything?"
    hide noahWorriedTalk
    show noahWorriedTalk2
    mitsue "I guess this guy did."
    hide noahWorriedTalk2
    show mitsueTalkUpL
    mitsue "You're just in time! Come in, take a seat."
    hide mitsueTalkUpL
    show akiNormal
    mitsue "Alright so, you guys know Aki. She's gonna be our DM."
    hide akiNormal

    # Choices time.
    menu:
        mitsue "Do you want me to explain how DnD works?"
        "Sure, that would help.":
            jump dndExplain
        "Nah, we got it.":
            label endExplain:
                "..."
    mitsue "Awesome-possum! Then let's get started with your characters..."

    # Choose a race.
    menu:
        "Choose your race!:"
        "Human":
            $human      = True
            $raceString = "human"
        "Elf":
            $elf        = True
            $raceString = "elf"
        "Dwarf":
            $dwarf      = True
            $raceString = "dwarf"
        "Goblin":
            $goblin     = True
            $raceString = "goblin"
        "Dragonborn":
            $dragonborn = True
            $raceString = "dragonborn"
        "Tabaxi":
            $tabaxi     = True
            $raceString = "tabaxi"
    
    
    # Choose a class.
    menu:
        "Now choose a class!:"
        "Barbarian":
            $barbarian   = True
            $classString = "barbarian" 
        "Fighter":
            $fighter     = True
            $classString = "fighter"
        "Monk":
            $monk        = True
            $classString = "monk"
        "Ranger":
            $ranger      = True
            $classString = "ranger"
        "Paladin":
            $paladin     = True
            $classString = "paladin"
        "Bard":
            $bard        = True
            $classString = "bard"
    "..."
    "{i}This was harder than she said. So complicated!{/i}"
    show akiTalk
    aki "Everybody done?"
    aki "..."
    aki "Nice!"
    aki "You’re all having a fine beverage at a tavern, where fate had pulled you all together."
    aki "Please present yourselves!"
    "..."
    y "Uhm, how?"
    hide akiTalk
    show mitsueTalkUpL
    mitsue "I guess I'll go first!"
    mitsue "So, uhm, I go by the name of Ara."
    mitsue "I’m a little moon elf that went down with the rogue life."
    mitsue "Wait, I have a drawing of how my character looks..."
    "Shitty drawing...(TODOO)"
    hide mitsueTalkUpL
    show mitsueClosedSmile
    mitsue "I promise not to steal your gold!"
    hide mitsueClosedSmile
    show akiTalk
    aki "Adorable. Anybody else? Noah?"
    hide akiTalk
    show noahTalk
    noah "Uh, sure."
    noah "Valmin here, the halfling bard."
    noah "I travelled up and down, earning my money through performances!"
    noah "I have this big coat with feathers and my trusty lute,"
    noah "which is just an old medieval guitar haha."
    hide noahTalk
    show noahSmile
    "Everybody laugh"
    "{i}Heh{/i}"
    hide noahSmile
    show akiTalk
    aki "Ok, Michael?"
    hide akiTalk
    show michaelTalkSideL
    michael "Oh, well."
    michael "I’m Melchior and I’m a wizard…"
    "..."
    y "That's all?"
    hide michaelTalkSideL
    show michaelQuiestioningTalkFronL
    michael "Well, you know the drill: pointy hat, cape, a wand or something, but it’s in nicer colors."
    michael "Look, my only objective is to find this rare sapphire, ok?"
    hide michaelQuiestioningTalkFronL
    show akiTalk
    aki "Interesting. [y]?"
    y "Ugh..."
    "{i}Let's just get this over with...{/i}"
    hide akiTalk
    show akiSmile
    y "Hello, I am a [raceString] [classString]..."
    hide akiSmile
    show akiTalk
    aki "And your name?"
    y "Just [y]. I like my name."
    aki "Alright, then let the adventure...BEGIN!"
    hide akiTalk

    # Exit scene.
    scene blackk with fade
    scene white with fade
    all "W-what?!"
    pause
return 











