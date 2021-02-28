import os, sys, getopt

from common import *
from const import *

fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]
for currentArgument in argumentList:
    if currentArgument in ("--relay"):
        setting = 1
    elif currentArgument in ("--break-heart"):
        setting = 2
    elif currentArgument in ("--custom"):
        setting = 3


source = BUFFER_DIR + 'buffer'
dest = BUFFER_DIR + 'buffer_new'
os.rename(source, dest) 

dialog = Dialog('print')
player = "alice"
bob_socket, bob_aes = setup(player, BUFFER_DIR, "buffer_new")

dialog = Dialog('print')
player = "bob"
alice_socket, alice_aes = setup(player, BUFFER_DIR, BUFFER_FILE_NAME)

if setting == 1:
    alice_msg = receive_and_decrypt(alice_aes, alice_socket)
    encrypt_and_send(alice_msg, bob_aes, bob_socket)
    dialog.chat('Alice said: "{}"'.format(alice_msg))
    bob_msg = receive_and_decrypt(bob_aes, bob_socket)
    tear_down(bob_socket, BUFFER_DIR, "buffer_new")
    encrypt_and_send(bob_msg, alice_aes, alice_socket)
    tear_down(alice_socket, BUFFER_DIR, BUFFER_FILE_NAME)
    dialog.chat('Bob said: "{}"'.format(bob_msg))

else:

    received = receive_and_decrypt(alice_aes, alice_socket)
    dialog.chat('Alice said: "{}"'.format(received))

    if setting == 3:
        dialog.prompt('Please input message for Bob...')
        to_send = input()
    else:
        to_send = BAD_MSG["alice"]
    encrypt_and_send(to_send, bob_aes, bob_socket)
    dialog.info('Message sent to Bob! Waiting for reply...')
    received = receive_and_decrypt(bob_aes, bob_socket)
    tear_down(bob_socket, BUFFER_DIR, "buffer_new")
    dialog.chat('Bob said: "{}"'.format(received))

    dialog.info("Waiting for message...")

    if setting == 3:
        dialog.prompt('Please input message for Alice...')
        to_send = input()
    else:
        to_send = BAD_MSG["bob"]
    encrypt_and_send(to_send, alice_aes, alice_socket)
    tear_down(alice_socket, BUFFER_DIR, BUFFER_FILE_NAME)
    dialog.info('Message sent to Alice!')


