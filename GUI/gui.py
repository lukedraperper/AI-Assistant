import copy
import threading
import tkinter
from main import Responder
import tkinter as tk
from tkinter import Frame


class GUI(object):
    """build the game UI"""
 
    # GLOBALS
    chat_log = None
    chat_log_input = None
 
    def __init__(self):
        # root business
        self.root = tk.Tk()
        self.root.title("JARVIS")
 
        # chat_frame
        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.grid(row=0, column=0, sticky='nsew')
        self.chat_log_title = None
        self.scroll = None
        self.chat_log_submit = None

        # right frame
        self.right_frame = tk.Frame(self.root, bg='black')
        self.right_frame.grid(row=0, column=1, sticky='nsew')
        self.html_frame = None
 
        # bindings
        self.root.bind("<Return>", LOGGER.receive)
 
    def build(self):
        """ put it all together"""
        self.compileChatFrame()
        self.loadWebsite()
        self.root.mainloop()
 
    def compileChatFrame(self):
        self.font = ('Helvetica', 12)  # Change the font family and size here
        """build the chat log frame widget"""
 
        # chat log title
        self.chat_log_title = tk.Label(self.chat_frame, text='Chat Log', font=self.font)
        self.chat_log_title.grid(row=0, column=0, sticky=tk.W)
 
        # chat log
        GUI.chat_log = tk.Text(self.chat_frame, font=self.font)
        GUI.chat_log.config(state=tk.DISABLED)
        GUI.chat_log.tag_configure(tagName=COMMAND_LOG_TYPE, foreground='purple')
        GUI.chat_log.tag_configure(tagName=NARRATOR_LOG_TYPE, foreground='#0000A0')
        GUI.chat_log.tag_configure(tagName=PLAYER_LOG_TYPE, foreground='black')
        GUI.chat_log.tag_configure(tagName=SYSTEM_LOG_TYPE, foreground='#FF00FF')
        GUI.chat_log.grid(row=1, column=0, sticky='nsew')
 
        # chat input
        GUI.chat_log_input = tk.Entry(self.chat_frame, background='gray', font=self.font)
        GUI.chat_log_input.grid(row=2, column=0, sticky='ew')
        GUI.chat_log_input.focus()
 
        # chat submit
        self.chat_log_submit = tk.Button(self.chat_frame, text='Submit', command=LOGGER.receive, font=self.font)
        self.chat_log_submit.grid(row=2, column=1, sticky='ew')
 
        # scrollbar
        self.scroll = tk.Scrollbar(self.chat_frame, orient=tk.VERTICAL, command=GUI.chat_log.yview)
        self.scroll.grid(row=1, column=2, sticky='ns', rowspan=2, padx=(5, 0))
        GUI.chat_log.configure(yscrollcommand=self.scroll.set)



        # Set row and column weights for the root to expand both frames
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

class Logger(object):
    """
    this class controls how messages are sent to the chat log
    fn: bm: update gr with the message and message type. this MUST be done prior to sending
    fn: receive: called by pressing enter or submit while the chat input is active
    fn: transmit: called be receive and does the actual work of sending the message to the chat log
    fn: capture: called when player input is needed to be captured and/or stored
 
    ex:
 
    """
 
    def __init__(self):
        self.message = None
        self.message_type = None
        self.received = False
        self.stored = None
 
    def bm(self, message, message_type):
        """update the GR with a new message so it can be sent using receive/transmit"""
 
        self.message_type = message_type
 
        if self.message_type == PLAYER_LOG_TYPE:
            self.message = '[You]:  ' + message
        elif self.message_type == SYSTEM_LOG_TYPE:
            self.message = '[System]:  ' + message
        elif self.message_type == NARRATOR_LOG_TYPE:
            self.message = '[JARVIS]:  ' + message
        elif self.message_type == COMMAND_LOG_TYPE:
            self.message = '[Command]:  ' + message
        else:
            self.message = message

    def process_message(self, message):
        """
        Process incoming messages and generate responses.
        This is a placeholder function and should be implemented based on your application logic.
        """
        # This is a placeholder response generation logic.
        response = Responder(message)
        return response
 
    def transmit(self):
        """transmit the message to the chat log"""
        
        if self.message:
            GAME_UI.chat_log.config(state=tkinter.NORMAL)
            GAME_UI.chat_log.insert(tkinter.END, "\n" + self.message)
            GAME_UI.chat_log_input.delete(0, tkinter.END)
 
            # attempt to find a message type for coloring
            if self.message_type is not None:
                pattern = '[' + self.message_type + ']:'
                GAME_UI.color_message_type(pattern=pattern, tag=self.message_type)
 
            GAME_UI.chat_log.see("end")
            GAME_UI.chat_log.config(state=tkinter.DISABLED)
        else:
            print('attempted to transmit an empty message')
            GAME_UI.chat_log.config(state=tkinter.NORMAL)
            GAME_UI.chat_log_input.delete(0, tkinter.END)
            GAME_UI.chat_log.see("end")
            GAME_UI.chat_log.config(state=tkinter.DISABLED)
 
        # reset variables after transmitting
        self.message = None
        self.message_type = None
 
    def receive(self, event=None):
        """use to capture player input"""
 
        # wait for player response
        self.message = GAME_UI.chat_log_input.get()
 
        # when message is found
        if self.message:
            self.message_type = PLAYER_LOG_TYPE
            # execute command
            if self.message[0] == '/':
                COMMANDS.command = self.message
                self.message, continue_command = COMMANDS.runCommand()
                if continue_command is True:
                    self.message_type = COMMAND_LOG_TYPE
                    LOGGER.bm(self.message, self.message_type)
                    self.transmit()
            else:
                response = self.process_message(self.message)
                # keep last thing typed by player in memory, currently overwrite each time
                # do not store commands
                if self.message_type == PLAYER_LOG_TYPE:
                    self.stored = copy.deepcopy(self.message)
 
                # send the non-command message
                if self.message is None:
                    LOGGER.bm(self.stored, self.message_type)
                else:
                    LOGGER.bm(self.message, self.message_type)
                self.transmit()

                if response is not None:
                    self.bm(response, NARRATOR_LOG_TYPE)
                    self.transmit()
                self.received = True
 
    def capture(self):
        """whenever a player value needs to be stored
           works by keeping track of whether the value has been stored or not"""
 
        self.received = False
        self.message_type = PLAYER_LOG_TYPE
 
        # wait for keypress
        while LOGGER.received is False:
            continue
 
        return LOGGER.stored
    
    
 
 
class Commands(object):
 
    # commands
    _HELP = '/help'
    _STATUS = '/status'
    _START_CHAT = '/start chat'
    _COMMAND_LS = [_HELP, _STATUS, _START_CHAT]
 
    def __init__(self, command):
        self.command = command
 
    def runCommand(self):
 
        # check if command is valid
        if self.command not in self._COMMAND_LS:
            message = ("'%s' is not a valid slash command. Type '/help' to see a list of commands." % self.command)
            return message, True
 
        if self.command in self._COMMAND_LS:
            # the help command
            if self.command == self._HELP:
                message = self.getCommands(self)
                return message, True
 
    @staticmethod
    def getCommands(self):
        """ give player a list of valid commands """
 
        message = " Available commands:"
        for c in self._COMMAND_LS:
            message += '\n ' + c
 
        return message
 
 
if __name__ == '__main__':
    # core stuff
    PLAYER = None
    COMBAT_STATE = False
 
    # logging stuff
    COMMAND_LOG_TYPE = 'Command'
    NARRATOR_LOG_TYPE = 'JARVIS'
    PLAYER_LOG_TYPE = 'Luke'
    SYSTEM_LOG_TYPE = 'System'
 
    # build the classes
    COMMANDS = Commands(command=None)
    LOGGER = Logger()
    GAME_UI = GUI()
    GAME_UI.build()