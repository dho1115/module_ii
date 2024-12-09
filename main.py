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
   ANYHOO... with this new and improved version, you can add color (I think it's red, green and yellow and maybe a few more) by doing color='color name' in the parameters. In addition, you can add border with the new and improved print with border = '*' and then it will add a '***' border. Don't like '*' border? Add your own!!!
   """
   from sys import stdout
   from colorama import init;
   from termcolor import colored;

   init();

   string= border(borderType=borderType, text=f'{caption}{sep.join(objects[0].split())}') if borderType else f'{caption}{sep.join(objects[0].split())}';

   if not color:
      stdout.write(string + end);
   else:
      stdout.write(colored(string, color=color, attrs=["bold", "blink"]) + end);

#TESTS.
print("THIS SHOULD BE RED...", sep=' - ', end='\n\t===== NEW LINE HERE. =====\n', color='red', caption='changed the caption:');
print("This should be GREEN and have a border of 0", borderType="0", sep=".", color='green');
print("THIS IS HOW YOU DO A BORING OLD PRINT (SEE BELOW)", caption='');
print(print.__doc__, caption='');




