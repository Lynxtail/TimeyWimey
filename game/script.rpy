# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# define e = Character('Эйлин', color="#c8ffc8")
define narrator = Character(None, kind = nvl, what_color="#000000", size = 12)
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    image bg old_diary = Image('images/bg.png')
# Игра начинается здесь:
label start:
    menu: 
        "Зайти в меню разнообразного дебага": 
            $ debug_mode = True
            jump debug_menu 
        "Пропустить вступление": 
            jump the_very_start_lazlo_nooptions
        "Начать вступление": 
            label the_very_start: 
                #show screen nvl
                nvl clear 
                hide screen nvl 
                scene bg old_diary
                $ renpy.pause(None) 
                " — Вэлкам ту зе клаб, бадди"


