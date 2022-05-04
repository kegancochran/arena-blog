import eel

eel.init('web')

@eel.expose
def niceButton():
    nice = 'nice'
    print(nice)
    return nice

eel.start('index.html', mode= 'default')
