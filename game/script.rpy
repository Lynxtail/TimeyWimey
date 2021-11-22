# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

# define e = Character('Эйлин', color="#c8ffc8")
# define narrator = Character("Рассказчик", kind = nvl, what_color="#ffffff", what_italic=True)

define narrator = nvl_narrator
define tmp = Character("???", kind = nvl, what_italic=False)

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# define menu = nvl_menu

# Игра начинается здесь:
label start:
    menu: 
        "Зайти в меню разнообразного дебага": 
            $ debug_mode = True
            jump debug_menu 
        "Пропустить вступление": 
            jump the_very_start_nooptions
        "Начать вступление": 
            jump the_very_start
    
    return

label the_very_start:
    nvl clear 
    hide screen nvl 
    scene bg old_diary
    $ renpy.pause(None) 
    narrator "Это было давным-давно..."
    # with fade
    nvl clear
    menu:
        "Для начала необходимо выбрать сценарий:"
        
        "Выбрать *сценарий_1*":
            jump scenario_1
            
        "Выбрать *сценарий_2*":
            jump scenario_2

label the_very_start_nooptions:
    return
    
label debug_menu:
    return

label scenario_1:
    nvl clear
    "Был выбран *сценарий_1*, в котором *описание_сценария*"
    
    menu:
        "Как вас зовут?"
        "Джон":
            tmp "Привет, Джон!"
            $ pass
        "Генри":
            tmp "Привет, Генри!"
            $ pass
    
    return

label scenario_2:
    nvl clear
    "Был выбран *сценарий_2*, который ещё не готов"
    return