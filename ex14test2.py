from sys import argv

script, user_name, answer_me = argv
prompt = '> '

user_name = raw_input()

print "Hi %s my name is %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Will you respond %s?" % answer_me
respond = raw_input(prompt)

print "What is your last name %s?" % user_name
name = raw_input(prompt)

print "Did you respond %s or not?" % answer_me
reply = raw_input(prompt)

print """
So your name is %s %s 
And you responded %s?
""" %(user_name, name, reply)