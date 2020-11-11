define michael = Character("Michael")
define noah = Character("Noah")
define mitsue = Character("Mitsue")
define aki = Character("Aki")
define all = Character("All")
define orc = Character("Orc")
define none = Character("???")

# --------------- Mitsue ---------------

# Normal world.
image mitsueSmile = "mitsueSmile.png"
image mitsueSmileUpL = "mitsueSmileUpL.png"
image mitsueClosedSmile = "mitsueClosedSmile.png"
image mitsueSurprisedTalk = "mitsueSurprisedTalk.png"
image mitsueWinkSmile = "mitsueWinkSmile.png"
image mitsueWorriedTalk = "mitsueWorriedTalk.png"
image mitsueTalkUpL = "mitsueTalkUpL.png"

# Dnd world.
image mitsuedndWinkTalk = "mitsuedndWinkTalk.png"
image mitsuedndWorriedTalk = "mitsuedndWorriedTalk.png"
image mitsuedndWorriedSmile = "mitsuedndWorriedSmile.png"
image mitsuedndWinkSmile = "mitsuedndWinkSmile.png"
image mitsuedndSmile = "mitsuedndSmile.png"
image mitsuedndTalkUpL = "mitsuedndTalkUpL.png"

# --------------- Michael ---------------

# Normal world.
image michaelNormal = "michaelNormal.png"
image michaelQuiestioningSideL = "michaelQuiestioningSideL.png"
image michaelQuiestioningTalkFronL = "michaelQuiestioningTalkFronL.png"
image michaelSmile1 = "michaelSmile1.png"
image michaelSurprised = "michaelSurprised.png"
image michaelTalkSideL = "michaelTalkSideL.png"
image michaelWorriedSideL = "michaelWorriedSideL.png"

# Dnd world.
image michaeldndQuiestioningSideL = "michaeldndQuiestioningSideL.png"
image michaeldndWorriedSideL = "michaeldndWorriedSideL.png"
image michaeldndAnnoyed = "michaeldndAnnoyed.png"
image michaeldndSmile1 = "michaeldndSmile1.png"
image michaeldndSadSideL = "michaeldndSadSideL.png"
image michaeldndNormal = "michaeldndNormal.png"


# Aki
image akiNormal = "akiNormal.png"
image akiSmile = "akiSmile.png"
image akiTalk = "akiTalk.png"

# --------------- Noah ---------------

# Normal world.
image noahConfidentTalk = "noahConfidentTalk.png"
image noahSmile = "noahSmile.png"
image noahSurprised = "noahSurprised.png"
image noahTalk = "noahTalk.png"
image noahWorriedSmile = "noahWorriedSmile.png"
image noahWorriedTalk = "noahWorriedTalk.png"
image noahWorriedTalk2 = "noahWorriedTalk2.png" 

# Dnd World.
image noahdndTalk = "noahdndTalk.png"
image noahdndWorriedTalk2 = "noahdndWorriedTalk2.png"
image noahdndWorriedTalk = "noahdndWorriedTalk.png"
image noahdndSurprised = "noahdndSurprised.png"
image noahdndSmile = "noahdndSmile.png"
image noahdndConfident = "noahdndConfident.png"

# Other.
image shittydrawing = "shittydrawing.png"

$ raceString = ""
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
    "{i}...{/i}"
    "{i}But you have to do stuff at a club!{/i}"
    "{i}I just want some peace and quiet…{/i}"
    $ y = renpy.input("{i}I'll just fill in my name.{/i}")
    while y == "":
        $ y = renpy.input("{i}I'll just fill in my name.{/i}")
    "..."
    y "{i}Whatever, I’ll decide tomorrow. I’m too tired for this!{/i}"
    y "{i}It’s not like the world will end by then.{/i}"
    y "{i}Wouldn’t be that bad if it did though.{/i}"
    # Stop music.

    scene outsideschool with fade
    y "{i}Ugh...{/i}"
    mitsue "Why the long face so early in the morning?"
    "..!"
    show mitsueSmile with fade
    y "Ah, mornin'!"
    hide mitsueSmile
    show mitsueSmileUpL
    "{i}And there she is! Our school’s Morning Glory… spreading joy or something.{/i}"
    "{i}Mitsue’s a little too much for me at times and- oh, ok, walk with me, sure.{/i}"
    "{i}There it goes, my peaceful morning.{/i}"
    "{i}Actually, wait. This bubbly blue-head should know some oke-ish clubs.{/i}"
    "{i}...{/i}"
    hide mitsueSmileUpL
    show mitsueSmile
    y "Hey..."
    y "Have you signed up for any clubs?"
    hide mitsueSmile
    show mitsueClosedSmile
    mitsue "Of course!"
    hide mitsueClosedSmile
    show mitsueWinkSmile
    mitsue "I’m in the art club, although I just ignore the tasks they give me."
    y "Oh, ok-"
    hide mitsueWinkSmile
    show mitsueSmileUpL
    mitsue "There’s also the DnD club."
    hide mitsueSmileUpL
    show mitsueWorriedTalk
    mitsue "Aki and I came up with it, but we need more members…"
    "{i}No wait, don’t ask me…{/i}"
    hide mitsueWorriedTalk
    show mitsueWinkSmile
    mitsue "Why don't you join our club?"
    "{i}I wasn’t thinking about a you-directed club but ok--{/i}"
    y "Sure... I'll drop by later"
    hide mitsueWinkSmile
    show mitsueClosedSmile
    mitsue "Awesome-possum! We meet up after school."
    y "Ok, well… I gotta go that way. See you later."
    hide mitsueClosedSmile
    show mitsueWinkSmile
    mitsue "Bye-bye!"
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
            $raceString = "human"
        "Elf":
            $raceString = "elf"
        "Dwarf":
            $raceString = "dwarf"
        "Goblin":
            $raceString = "goblin"
        "Dragonborn":
            $raceString = "dragonborn"
        "Tabaxi":
            $raceString = "tabaxi"
    
    
    # Choose a class.
    menu:
        "Now choose a class!:"
        "Barbarian":
            $classString = "barbarian" 
        "Fighter":
            $classString = "fighter"
        "Monk":
            $classString = "monk"
        "Ranger":
            $classString = "ranger"
        "Paladin":
            $classString = "paladin"
        "Bard":
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
    hide mitsueTalkUpL
    show shittydrawing
    pause
    hide shittydrawing
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

    # Chapter 1 - Tavern
    scene tavern with fade
    y "Excuse me, but what the HECK?!"
    y "You guys can see that, right?"
    y "I'm not hallucinating, am I?"
    show michaeldndQuiestioningSideL
    michael "I'm not sure we're somewhere else..."
    y "Uh...Mitsue? Any explanation would help right now."
    hide michaeldndQuiestioningSideL
    show mitsuedndWorriedTalk
    mitsue "I might have forgotten to mention the teleportation part..."
    hide mitsuedndWorriedTalk
    show mitsuedndWinkSmile
    mitsue "Oopsies!"
    hide mitsuedndWinkSmile
    show noahdndWorriedTalk
    noah "That was kind of a dick move, but..."
    hide noahdndWorriedTalk
    show noahdndTalk
    noah "I like this outfit, not gonna lie."
    y "Wait...where's Aki?"
    hide noahdndTalk
    show mitsuedndWorriedSmile
    mitsue "Ok, don't freak out, but..."
    mitsue "she'll appear as a voice inside out heads hahaa..."
    y "Ok, fine. So let me get this straight: We're in this fantasy world where we look just like the characters we created earlier, right?"
    hide mitsuedndWorriedSmile
    show mitsuedndSmile 
    mitsue "That's right!"
    y "And we'll...get home today...right?"
    mitsue "Obviously. We just have to solve a quest. The time in our world is much slower than the time here anyways."
    hide mitsuedndSmile
    show mitsuedndWorriedSmile
    mitsue "Just try to calm down. If your character dies, you return to your original world."
    hide mitsuedndWorriedSmile
    show mitsuedndWinkTalk
    mitsue "Now come on, we have a story to fulfill."
    hide mitsuedndWinkTalk
    aki "Ahem, if you're done freaking out..."
    show michaeldndWorriedSideL
    michael "No wait. I just feel stupid. I should have got a cooler attire."

    menu:
        "You look fine. [+5]":
            show michaeldndSmile1
            michael "I guess I can make it work."
            hide michaeldndSmile1
        "Does it really matter? [+1]":
            show michaeldndAnnoyed
            michael "Not that much, apparently..."
            y "..."
            hide michaeldndAnnoyed
        "You look good in everything! [+3]":
            show michaeldndSadSideL
            michael "Yeah, everything but this."
            hide michaeldndSadSideL
    show mitsuedndSmile
    mitsue "Anyways! We should look for a simple quest."
    hide mitsuedndSmile
    y "How about that guy?"
    y "{i}I point at a half-ord{/i}"
    y "He looks like he's got a quest."
    show mitsuedndWinkTalk
    mitsue "You're right! We should go talk to him."
    hide mitsuedndWinkTalk
    show noahdndSurprised
    noah "Wait, I'll try"
    hide noahdndSurprised
    show mitsuedndWinkSmile
    mitsue "Oho! We love an enthusiastic player!"
    hide mitsuedndWinkSmile

    menu: 
        "Ha! Nerd. [+0]":
            show noahdndWorriedTalk 
            noah "Yeah, well. We're stuck here, might as well have some fun"
            y "..."
            hide noahdndWorriedTalk
        "Never took you for this kind of stuff [+2]":
            show noahWorriedTalk2 
            noah "Well, we should have fun while we're here."
            noah "DnD is supposed to be fun. Our advenutre just has better visuals."
            y "I guess that's true..."
            hide noahWorriedTalk2

    y "{i}Ok, let's do this. Get them, boy!{/i}"
    show noahdndTalk
    noah "Ahem...excuse me, good sir."
    hide noahdndTalk
    show noahdndSmile
    noah "I was wondering if you would be in need of help."
    hide noahdndSmile
    orc "Hmm...I might have something for you."
    orc "You see...far in the forest lives a dear persone of mine."
    orc "You wouldn't mind giving her these flowers for me, would you?"
    orc "I won't be able to get there soon enough."
    show mitsuedndWinkTalk
    mitsue "We can do that!"
    hide mitsuedndWinkTalk
    show mitsuedndSmile
    mitsue "Where exactly in the forest?"
    hide mitsuedndSmile
    orc "Just follow the long path and take the first left. She doesn't live far from there."
    orc "Here. Make sure you give these before the sun sets."
    orc "Find me tomorrow for payment."
    show noahdndConfident
    noah "We won't disappoint you, sir."
    hide noahdndConfident
    show mitsuedndSmile
    mitsue "Ok, guys. Let's go."
    hide mitsuedndSmile

    # Forest.
    scene forest with fade
    y "How do we know this is not a scam?"
    show mitsuedndTalkUpL
    hide mitsuedndTalkUpL
    show mitsuedndWorriedSmile
    mitsue "I guess Aki's taking care of it?"
    mitsue "She's like a God in this world, although there are things she can't do."
    mitsue "I mean, she knows the story and we'll progress some way or another,"
    mitsue "but this is your first time here, so we're taking it easy."
    y "Ok, that makes sense."
    "..."
    hide mitsuedndWorriedSmile
    show mitsuedndWorriedTalk
    mitsue "Look. I know this is a lot to take in. We didn't really mean to trick you guys to come here, but..."
    hide mitsuedndWorriedTalk
    show mitsuedndWorriedSmile
    mitsue "I doubt you would have believed me if I told you we were gonna transcend time and space to get to a magical place."
    mitsue "I mean, come on."
    y "No, no, you're right. I would have thought you really lost it if you pulled that one on me."
    hide mitsuedndWorriedSmile
    show noahdndTalk
    noah "I like it!"
    hide noahdndTalk
    show mitsuedndWinkTalk
    mitsue "Haha, really?"
    hide mitsuedndWinkTalk
    show noahdndSmile
    noah "Yeah, I thought we were just going to play a table game, but this is on another level."
    hide noahdndSmile
    show michaeldndSmile1
    michael "Yeah. I mean, except for this outfit, this is really cool."
    hide michaeldndSmile1
    show michaeldndQuiestioningSideL
    michael "That, or we got high without realizing it."
    hide michaeldndQuiestioningSideL
    show michaeldndWorriedSideL
    michael "Uh, sorry to interrupt, but the path branches here."
    hide michaeldndWorriedSideL

    # Forest 2.
    scene forest2 with fade
    menu: 
        "Go left [main story]":
            show mitsuedndSmile
            mitsue "He said her house is not far from here, right?"
            hide mitsuedndSmile
            show mitsuedndWorriedTalk
            mitsue "What time is it?"
            hide mitsuedndWorriedTalk
            show mitsuedndSmile
            y "I feel like time's pretty relative here, but we should hurry a litte."
            hide mitsuedndSmile
            none "Not so fast, travelers!!"
            y "Huh!?"
        "Go right":
            show michaeldndNormal 
            michael "We've been waling for a while."
            hide michaeldndNormal
            show michaelWorriedSideL
            michael "Are you sure he didn't say to go left?"
            hide michaelWorriedSideL
            show mitsuedndWorriedTalk
            mitsue "Now that you mention it...maybe we should go back."
            hide mitsuedndWorriedTalk
    pause
return 











