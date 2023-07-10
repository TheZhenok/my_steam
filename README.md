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

# WishList
>> user

>> games

# Order
>> user

>> game

>> datetime_buy

>> method (наличка или картой например)

>> money

# Invite card
>> самостоятельно
