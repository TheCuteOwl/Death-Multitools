from pystyle import Anime, Colorate, Colors, Center, System
import time
from Utils import *
import platform
import sys

def set_terminal_title(title):
    if platform.system() == 'Windows':
        sys.stdout.write("\033]0;{}\007".format(title))
    else:
        sys.stdout.write("\033]2;{}\007".format(title))
    sys.stdout.flush()



ascii = '''

██████╗░███████╗░█████╗░████████╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║░░██║
██║░░██║█████╗░░███████║░░░██║░░░███████║
██║░░██║██╔══╝░░██╔══██║░░░██║░░░██╔══██║
██████╔╝███████╗██║░░██║░░░██║░░░██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝'''[1:]

banner = '''

                                                                                                                                                                                
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                           .@@@@                                                                                                         @@@@(                                          
                                           *@@@@@@(                                                                                                   .@@@@@@%                                          
                                              @@@@@@*                                                                                                @@@@@@,                                            
                                                 &@@@@@                                                                                           @@@@@@                                                
                                                    @@@@@                                                                                       #@@@@,                                                  
                                                       @@@                                                                                     &@@,                                                     
                                                    .@@@@@.                                                                                    @@@@@(                                                   
                                                   @@@@@                                                                                         @@@@@#                                                 
                                                 @@@@@@                                                                                           (@@@@@                                                
                                                @@@@@&                                                                                             *@@@@@                                               
                                               #@@@@@                                        ,             /                                        @@@@@@                                              
                                               @@@@@@                                      .@               %(                                      @@@@@@                                              
                                               @@@@@@.                                   /@/                  @&                                    @@@@@@                                              
                                               #@@@@@@                                 @@@                     @@@                                 @@@@@@@                                              
                                                @@@@@@@                             *@@@                         @@@%                             @@@@@@@                                               
                                                 @@@@@@@@                        &@@@@                             @@@@@                        @@@@@@@@                                                
                                                   @@@@@@@@@%              .%@@@@@@&                                 (@@@@@@&,              /@@@@@@@@@.                                                 
                                                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@                                       (@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                    
                                                        ,@@@@@@@@@@@@@@@@@@@&                                               #@@@@@@@@@@@@@@@@@@@#                                                       
                                                                .*/*,                                                               .*/*,                                                               
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                    
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                       '''

Tools = """


    ┌────────────────────┬┐        ┌┬───────────────────┬┐        ┌┬───────────────────┬┐
  ┌─┤[1]Fake Image Logger│┼────────┼│                   │┼────────┼│                   ││
  │ └────────────────────┴┘        └┴───────────────────┴┘        └┴───────────────────┴┘
  │
  │ ┌────────────────────┬┐        ┌┬───────────────────┬┐        ┌┬───────────────────┬┐
┌─┼─┤[2]Fake Vouch       │┼────────┼│                   │┼────────┼│                   ││
│ │ └────────────────────┴┘        └┴───────────────────┴┘        └┴───────────────────┴┘
│ │
│ │ ┌────────────────────┬┐        ┌┬───────────────────┬┐        ┌┬───────────────────┬┐
└─┼─┤[3]Token Checker    │┼────────┼│                   │┼────────┼│                   ││
  │ └────────────────────┴┘        └┴───────────────────┴┘        └┴───────────────────┴┘
  │
  │ ┌────────────────────┬┐        ┌┬───────────────────┬┐        ┌┬───────────────────┬┐
  └─┤                    │┼────────┼│                   │┼────────┼│                   ││
    └────────────────────┴┘        └┴───────────────────┴┘        └┴───────────────────┴┘

"""

def init():
    System.Clear()
    System.Size(200, 50)
    Anime.Fade(text=Center.Center(banner), color=Colors.red_to_black, mode=Colorate.Diagonal, enter=True)
   
init()
def main():
   System.Clear()
   set_terminal_title("Death Tools")
   print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(ascii)))
   print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(Tools)))
   a = input(Center.XCenter(Colorate.Diagonal(Colors.blue_to_cyan, "─►")))
   if a == '1':
      from Utils import FakeIMGLog
      System.Clear()
   elif a == '2':
      from Utils import FakeVouch
   elif a == '3':
      from Utils import TokenChecker
   else: 
      print('Wrong Input')
      time.sleep(0.75)
      System.Clear()
      main()

while True:
   main()

