import f, lps, psn, psw

if f.test() and lps.test() and psn.test() and psw.test(): print('All scripts loaded.')
else: print('An error ocurred.'), exit()

print('Please do not use this toolkit in a way which harasses the 1990 Computer Misuse Act.\nThis toolkit only has over-simple/basic tools and their are also lots of bugs, as this is the developer\'s first time writing full code, sorry.') 
userscmd = str(input('chaos>>> '))
#if anyone is here but my lonley self i have a question
#is 6earlyhuman a good or bad music artist
#bc ik rn theirs alot of hate on scenecore

try: f.process_cmd(userscmd) 
except BaseException as e: print(f'Toolkit closed down. Reason:{e.args}')
