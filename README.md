# Steam

> ## Models
> Game

> Order

> User

> InviteCard

> Genres

> WishList

> Company

> Comment

# Game
>> name

>> price

>> genres(m)

>> company

>> datetime_created

>> comments(o-o)


# Company
>> name

>> datetime_created

>> comment(o-o)


# Comment
>> user

>> text (MABY NULL)

>> rate
