from sys import stdout
from colorama import init;
from termcolor import colored;

init();
#Auxillary function that adds border feature.
def border(borderType="*", text='INSERT TXT HERE'):
   """This border function adds a border feature to the new and improved print function (below)."""
   TopAndBottomborder=borderType*len(text) + (borderType*5)
   borderedText = f"\n\n\n{TopAndBottomborder}\n{borderType} {text}  {borderType}\n{TopAndBottomborder}\n\n\n";
   return borderedText;

def print(*objects, end='\n', sep=' ', color=False, borderType=None, caption="Output from the NEW & IMPROVED Print => "):
   """
   The New and improved print() function which comes with new and improved features!!!
   There MAY be more to come later...
   If I can get around to it.
   """
   string= border(borderType=borderType, text=f'{caption}{sep.join(objects[0].split())}') if borderType else f'{caption}{sep.join(objects[0].split())}';

   if not color:
      stdout.write(string + end);
   else:
      stdout.write(colored(string, color=color, attrs=["bold", "blink"]) + end);

print("THIS SHOULD BE RED...", sep=' - ', end='\n\t===== NEW LINE HERE. =====\n', color='red');
print("This should be GREEN and have a border of 0", borderType="0", sep="/", color='green');
print("Boring old print with no borders and no caption.", caption="")





