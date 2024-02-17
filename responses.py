import random


def handle_responses(message) -> str:
    p_message = message.lower()     # makes the user msg in lower case so we only need to code for lower case written only

    if p_message == 'help':
        return '''help?? *sounds like skill issue*
        but i will tell you all the following commands u can use:
        hello,roll,flip.'''
    
    if p_message == 'hello':
        return 'Hello hababi'

    if p_message == 'roll':
        return  'the number in your destiny is:',str(random.randint(1,100))

    if p_message == 'flip':
        c = str(random.randint(0,2))
        if c == '1':
            return '`The side in your destiny is: Heads`'
        else:
            return '`The side in your destiny is: Tails`'
    
    if p_message == 'how are you?':
        return 'jani mein ok hoon'
    
    if p_message == 'i am bored':
        return 'lets play a game then. Where you go touch some grass for a while'
    
    if p_message == 'open spotify':
        return ' no.'
    if p_message == 'thanks':
        return 'Glad i could help :)'
    
    

