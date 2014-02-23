# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
#    style.menu_choice_button_text.drop_shadow = [(2, 2)]
#    style.textbutton_text.idle_color = "#b66478"
    style.bigass = Style(style.default)
    style.bigass.font = "AtomicClockRadio.ttf"
#    style.bigass.hover_color = "#b66478"   
#    style.bigass.idle_color = "#000" #"#b66478"
#    style.bigass.selected_color = "#fff" #"#8f4251"
    style.bigass.size = 26
#    style.bigass.drop_shadow = [(2, 2)]

##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    use quick_menu
        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        text "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n {color=#000}{size=-6}? 2012 Neko-Soft Gmbh{/color}{/size}"
    # The main menu buttons.
    frame:
        background None
        style_group "mm"
        xoffset 50
        yoffset 145
        #xoffset 25
        #yoffset 150

        has vbox

        imagebutton:
            ypadding 5
            action [Play("sound", "sfx/confirm2.ogg"), Start()]
            idle "gui/New1.png"
            hover "gui/New2.png"
            hovered Play ("sound", "sfx/slight.ogg")       
        imagebutton:
            ypadding 5
            action ShowMenu("load")
            idle "gui/Continue1.png"
            hover "gui/Continue2.png"
            hovered Play ("sound", "sfx/slight.ogg")            
        imagebutton:
            ypadding 5
            action ShowMenu("preferences")
            idle "gui/Options1.png"
            hover "gui/Options2.png"
            hovered Play ("sound", "sfx/slight.ogg")            
        imagebutton:
            ypadding 5
            action ShowMenu("mygallery")
            idle "gui/Gallery1.png"
            hover "gui/Gallery2.png"
            hovered Play ("sound", "sfx/slight.ogg")            
        imagebutton:
            ypadding 5
            action Quit(confirm=False)
            idle "gui/Quit1.png"
            hover "gui/Quit2.png"
            hovered Play ("sound", "sfx/slight.ogg")            
        
init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"

        
##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
       
        style "gm_root"
        #background "gui/game.png" 
        
    # The various buttons.
    frame:
        background None
        #style_group "gm_nav"
        xalign 0.5
        yoffset 1
        
        has hbox

        imagebutton:
            action (Play("sound", "sfx/cancel.ogg"), Return())
            idle "gui/Return1.png"
            hover "gui/Return2.png"
            hovered Play ("sound", "sfx/slight.ogg")     
        imagebutton:
            action ShowMenu("preferences")
            idle "gui/Options0.png"
            selected_idle "gui/Options1v2.png"
            hover "gui/Options2v2.png"
            hovered Play ("sound", "sfx/slight.ogg")                 
        imagebutton:
            action ShowMenu("save")
            idle "gui/Save0.png"
            selected_idle "gui/Save1.png"
            hover "gui/Save2.png"
            hovered Play ("sound", "sfx/slight.ogg")                 
        imagebutton:
            action ShowMenu("load")
            idle "gui/Load0.png"
            selected_idle "gui/Load1.png"
            hover "gui/Load2.png"
            hovered Play ("sound", "sfx/slight.ogg")                 
            
    frame:
        background None
        #style_group "gm_nav"
        xalign 0.5
        yoffset 730
        
        has hbox            
            
        imagebutton:
            action MainMenu()
            idle "gui/Main1.png"
            hover "gui/Main2.png"     
            hovered Play ("sound", "sfx/slight.ogg")                 
        imagebutton:
            action Help()
            idle "gui/Help1.png"
            hover "gui/Help2.png"
            hovered Play ("sound", "sfx/slight.ogg")                 
        imagebutton:
            action Quit()
            idle "gui/Quit1v2.png"
            hover "gui/Quit2v2.png"             
            hovered Play ("sound", "sfx/slight.ogg")                 
            
        
init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:

    frame:
        #style "file_picker_frame"
        background None
        yoffset 60 
        has hbox

        # The buttons at the top allow the user to pick a
        # page of files.
        vbox:
            xpos 200
            style_group "file_picker_nav"
            
            textbutton _(" Previous Page  "):
                action FilePagePrevious()
                background "gui/emptysel.png"
                #hover "gui/emptyhover.png"
                
#            textbutton _("Auto"):
#                action FilePage("auto")

#            textbutton _("Quick"):
#                action FilePage("quick")

            for i in range(1, 6):
                #textbutton str(i):
                vbox:
                    yminimum 200
                    #xpos 50
                    label _(" ")
                    textbutton _(" Slots Page [i]   "):
                       
                        action FilePage(i)
                        background "gui/emptyunsel.png"
                        #hover "gui/emptyhover.png"
                        #selected_idle "gui/emptysel.png"

            label _(" ")             
            textbutton _(" Next Page     "):
                action FilePageNext()
                background "gui/emptysel.png"
                #hover "gui/emptyhover.png"
                
        $ columns = 1
        $ rows = 4
                
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
#            yfill True
            xpos 260
            xmaximum 520
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True
                    yminimum 145
                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)
                    
                    # Format the description, and add it as text.
                    $ description = "% 2s. %s\n%s" % (
                        FileSlotName(i, columns * rows),
                        FileTime(i, empty=_("Empty Slot.")),
                        FileSaveName(i))

                    text description

                    key "save_delete" action FileDelete(i)
                    
                    
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu
    use navigation

    frame:
        background None
        foreground "savethis"
        #xalign 0.25
        #yalign 0.5    
        
    use file_picker        

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation

    frame:
        background None
        foreground "loadthis"
        #xalign 0.25
        #yalign 0.5    
        
    use file_picker  

init -2 python:
#    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_button.ypadding = 10

    style.file_picker_text = Style(style.large_button_text)

    config.thumbnail_width = 160
    config.thumbnail_height = 120



##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    frame:
        background None
        foreground "optionsthis"
        #xalign 0.25
        #yalign 0.5   

    # Put the navigation columns in a three-wide grid.
    grid 4 1:
        style_group "prefs"
        xfill True

        vbox:
            yoffset 60
            frame:
                background None
                style_group "pref"
                
        # The left column.
        vbox:     
            yoffset 60
            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")
                
            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton "Test":
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            #frame:
                #style_group "pref"
                #has vbox

                #label _("Voice Volume")
                #bar value Preference("voice volume")

                #if config.sample_voice:
                    #textbutton "Test":
                        #action Play("voice", config.sample_voice)
                        #style "soundtest_button"

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")

        vbox:
            yoffset 60
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                #textbutton _("Window") action Preference("display", "window")
                #textbutton _("Fullscreen") action Preference("display", "fullscreen")
                imagebutton:
                    action Preference("display", "window")
                    idle "gui/windowunsel.png"
                    hover "gui/windowhover.png"
                    selected_idle "gui/windowsel.png"
                    hovered Play ("sound", "sfx/slight.ogg")                         
                imagebutton:
                    action Preference("display", "fullscreen")
                    idle "gui/fullscreenunsel.png"
                    hover "gui/fullscreenhover.png"
                    selected_idle "gui/fullscreensel.png"
                    hovered Play ("sound", "sfx/slight.ogg")                         
                
            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                #textbutton _("All") action Preference("transitions", "all")
                #textbutton _("None") action Preference("transitions", "none")
                imagebutton:
                    action Preference("transitions", "all")
                    idle "gui/allunsel.png"
                    hover "gui/allhover.png"
                    selected_idle "gui/allsel.png"
                    hovered Play ("sound", "sfx/slight.ogg")                         
                imagebutton:
                    action Preference("transitions", "none")
                    idle "gui/noneunsel.png"
                    hover "gui/nonehover.png"
                    selected_idle "gui/nonesel.png"
                    hovered Play ("sound", "sfx/slight.ogg")                     
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
#                textbutton _("Seen Messages") action Preference("skip", "seen")
#                textbutton _("All Messages") action Preference("skip", "all")
                imagebutton:
                    action Preference("skip", "seen")
                    idle "gui/seenunsel.png"
                    hover "gui/seenhover.png"
                    selected_idle "gui/seensel.png"
                    hovered Play ("sound", "sfx/slight.ogg")     
                imagebutton:
                    action Preference("skip", "all")
                    idle "gui/allunsel.png"
                    hover "gui/allhover.png"
                    selected_idle "gui/allsel.png"
                    hovered Play ("sound", "sfx/slight.ogg")     
            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                #textbutton _("Stop Skipping") action Preference("after choices", "stop")
                #textbutton _("Keep Skipping") action Preference("after choices", "skip")
                imagebutton:
                    action Preference("after choices", "stop")
                    idle "gui/stopskipunsel.png"
                    hover "gui/stopskiphover.png"
                    selected_idle "gui/stopskipsel.png"
                    hovered Play ("sound", "sfx/slight.ogg")                         
                imagebutton:
                    action Preference("after choices", "skip")
                    idle "gui/keepskipunsel.png"
                    hover "gui/keepskiphover.png"
                    selected_idle "gui/keepskipsel.png"                    
                    hovered Play ("sound", "sfx/slight.ogg")     
#            frame:
#                style_group "pref"
#                has vbox

#                textbutton _("Begin Skipping") action Skip()                
                        
        vbox:
            yoffset 60
            frame:
                background None
                style_group "pref"
                
init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 218 #192
    style.pref_slider.ymaximum = 20
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0
    style.pref_label_text.size = 28
    style.pref_label_text.drop_shadow = [(2, 2)]

    style.pref_slider.left_bar = "gui/bar_full.png"
    style.pref_slider.right_bar = "gui/bar_empty.png"
    style.pref_slider.hover_left_bar = "gui/bar_hover.png"
    
    style.pref_slider.thumb = "gui/slider_thumb.png"
#   style.pref_slider.thumb_offset = 6
#    style.pref_slider.thumb_shadow = None        
    
    
##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True

    window:
        style "gm_root"        
        #background "gui/game.png"        


    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
#            textbutton _("Yes") action yes_action
#            textbutton _("No") action no_action
            imagebutton:
                action yes_action           
                idle "gui/yesidle.png"
                hover "gui/yeshover.png"
                hovered Play ("sound", "sfx/slight.ogg") 
                
            imagebutton:
                action no_action
                idle "gui/noidle.png"
                hover "gui/nohover.png"
                hovered Play ("sound", "sfx/slight.ogg") 

init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.size = 28    
    style.yesno_label_text.drop_shadow = [(2, 2)]

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:
    if not scenariomode:        
        imagebutton:
            idle "gui/day.png"
            hover "gui/day.png"
            xpos 0
            ypos 6
        window:
            xalign 0.1 yalign 0.02
            background None
            text "                   {=daylook}[currentday]{/=daylook}"          
            
    if buttonstats[0] == "normal":
        imagebutton:
            idle "bluesmalltrans"
            hover "bluesmall"
            xpos 50
            ypos 500
    if buttonstats[0] == "increasing":
        imagebutton:
            idle "bluesmallincrease"
            hover "bluesmall"
            xpos 50
            ypos 500
    if buttonstats[1] == "normal":            
        imagebutton:
            idle "orangesmalltrans"
            hover "orangesmall"
            xpos 112
            ypos 500
    if buttonstats[1] == "increasing":            
        imagebutton:
            idle "orangesmallincrease"
            hover "orangesmall"
            xpos 112
            ypos 500  
    if buttonstats[2] == "normal":            
        imagebutton:
            idle "pinksmalltrans"
            hover "pinksmall"
            xpos 170
            ypos 500
    if buttonstats[2] == "increasing":            
        imagebutton:
            idle "pinksmallincrease"
            hover "pinksmall"
            xpos 170
            ypos 500       
    if buttonstats[3] == "normal":            
        imagebutton:
            idle "greensmalltrans"
            hover "greensmal"
            xpos 231
            ypos 500
    if buttonstats[3] == "increasing":            
        imagebutton:
            idle "greensmallincrease"
            hover "greensmal"
            xpos 231
            ypos 500       
    
    imagebutton:
        action Skip()
        idle "gui/Skip.png"
        hover "gui/Skipglow.png"
        xpos 840
        ypos 515        
    # Add an in-game quick menu.
    vbox:
        style_group "quick"
    
        xalign 0.975
        yalign 0.93

#        textbutton _("{size=+8}Auto{/size}") action Preference("auto-forward", "toggle")
#        textbutton _("{size=+8}Prefs{/size}") action ShowMenu('preferences')
#        textbutton _("{size=+8}Save{/size}") action ShowMenu('save')        
#        textbutton _("{size=+8}Qsave{/size}") action QuickSave()
#        textbutton _("{size=+8}Qload{/size}") action QuickLoad()

    imagebutton:
        action Preference("auto-forward", "toggle")
        idle "gui/autoarrowtrans.png"
        hover "gui/autoarrow.png"
        selected_idle "gui/autoarrowsel.png"
        hovered [ Show("my_tooltip", my_text =Text("AUTO TOGGLE"), my_tt_xpos=860, my_tt_ypos=10) ] unhovered [Hide("my_tooltip")]        
        xalign 0.97
        yalign 0.79
        
    imagebutton:
        action Rollback()
        idle "gui/reversearrowtrans.png"
        hover "gui/reversearrow.png"
        hovered [ Show("my_tooltip", my_text =Text("ROLLBACK"), my_tt_xpos=900, my_tt_ypos=10) ] unhovered [Hide("my_tooltip")]                
        xalign 0.955
        yalign 0.825
#    if renpy.in_rollback:
#        $ ui.textbutton("V", clicked=renpy.roll_forward, xalign=0.95, yalign=0.92)

    imagebutton:
        action [Hide("my_tooltip"), ShowMenu('save')]
        idle "gui/floppytrans.png"
        hover "gui/floppy.png"
        hovered [ Show("my_tooltip", my_text =Text("SAVE"), my_tt_xpos=920, my_tt_ypos=10) ] unhovered [Hide("my_tooltip")]                
        xalign 0.955
        yalign 0.88
        
    imagebutton:
        action [Hide("my_tooltip"), ShowMenu('preferences')]
        idle "gui/gearstrans.png"
        hover "gui/gears.png"
        hovered [ Show("my_tooltip", my_text =Text("OPTIONS"), my_tt_xpos=900, my_tt_ypos=10) ] unhovered [Hide("my_tooltip")]                
        xalign 0.965
        yalign 0.95        

screen my_tooltip:
    add my_text xpos my_tt_xpos ypos my_tt_ypos        
        
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#D6D3CF"
    style.quick_button_text.hover_color = "#fff"
    style.quick_button_text.selected_idle_color = "#E4FD56"
    style.quick_button_text.selected_hover_color = "#FBCF04"
    style.quick_button_text.insensitive_color = "#B8B6B2"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False

screen cgnavigation:

    # The background of the game menu.
    window:
       
        style "gm_root"
        #background "gui/game.png" 
        
    # The various buttons.
    frame:
        background None
        #style_group "gm_nav"
        xalign 0.5
        yoffset 1
        
        has hbox

        imagebutton:
            action (Play("sound", "sfx/cancel.ogg"), Return())
            idle "gui/Return1.png"
            hover "gui/Return2.png"
            hovered Play ("sound", "sfx/slight.ogg")             
        imagebutton:
            action ShowMenu("mygallery")
            idle "gui/Pix0.png"
            selected_idle "gui/Pix1.png"
            hover "gui/Pix2.png"
            hovered Play ("sound", "sfx/slight.ogg")     
        imagebutton:
            action ShowMenu("mygallery2")
            idle "gui/Piks0.png"
            selected_idle "gui/Piks1.png"
            hover "gui/Piks2.png"                        
            hovered Play ("sound", "sfx/slight.ogg")     
        imagebutton:
            action ShowMenu("mymusic")
            idle "gui/Music0.png"
            selected_idle "gui/Music1.png"
            hover "gui/Music2.png"
            hovered Play ("sound", "sfx/slight.ogg")     
            
            
    frame:
        background None
        #style_group "gm_nav"
        xalign 0.5
        yoffset 730
        
        has hbox            
            
#        imagebutton:
#            action MainMenu()
#            idle "gui/Main1.png"
#            hover "gui/Main2.png"     
        imagebutton:
            action Help()
            idle "gui/Help1.png"
            hover "gui/Help2.png"
            hovered Play ("sound", "sfx/slight.ogg")                 
        imagebutton:
            action Quit()
            idle "gui/Quit1v2.png"
            hover "gui/Quit2v2.png"            
            hovered Play ("sound", "sfx/slight.ogg")         
# CG and music gallery

init python:
    
#Gallery

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.
 #   style.g.button.background=None
 #  style.g.button.hover_background=None

    # This button has multiple images assocated with it. We use unlock_image
    # so we don't have to call both .image and .unlock. We also apply a
    # transform to the first image.
    
    g.button("cgprologue") #Slot 1
    g.image("cg 00")
    g.image("cg 01")
    g.image("cg 03")
    g.image("cg 04")
    g.image("cg 05")

    g.button("cgtwo") #Slot 2   
    g.image("cg 20")
    
    g.button("cgthree") #Slot 3
    g.image("cg 30")
    
    g.button("cgfive") #Slot 4
    g.image("cg 50")
    
    g.button("cgseven") #Slot 5
    g.image("cg 70")
    
    g.button("cgeight") #Slot 6
    g.image("cg 80")
    g.image("cg 81")
    
    g.button("cgnine") #Slot 7
    g.image("cg 90")
    g.image("cg 91")
    g.image("cg 92")    
    
    g.button("cgten") #Slot 8
    g.image("cg 100")
    g.image("cg 101")
    
    g.button("cgeleven")
    g.image("cg 110")
    
    g.button("cge2")
    g.image("cg e2")
    
    g.button("cge3")
    g.image("cg e3")
    g.image("cg e3_1")
    g.image("cg e3b")
    
    g.button("cgb2")
    g.image("cg b2")
    g.image("cg b2_1")
    
    g.button("cgb3")
    g.image("cg b3")
    
    g.button("traincgs")
    g.image("alicesing")
    g.image("alicedance")
    
    # The transition used when switching images.
    g.transition = dissolve
   
# Step 3. The gallery screen we use.
screen mygallery:
    
    tag menu

    use cgnavigation

    frame:
        background None
        foreground "gallerythis"
    frame:
        xpos 31
        ypos 60
        xpadding 5
        ypadding 15        
        add g.make_button("cgprologue", "cg 00 t", "gui/cglock.png", "cg 00 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 273
        ypos 60
        xpadding 5
        ypadding 15        
        add g.make_button("cgtwo", "cg 20 t", "gui/cglock.png", "cg 20 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 517
        ypos 60
        xpadding 5
        ypadding 15        
        add g.make_button("cgthree", "cg 30 t", "gui/cglock.png", "cg 30 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 759
        ypos 60
        xpadding 5
        ypadding 15        
        add g.make_button("cgfive",  "cg 50 t", "gui/cglock.png", "cg 50 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 31
        ypos 260
        xpadding 5
        ypadding 15        
        add g.make_button("cgseven", "cg 70 t", "gui/cglock.png", "cg 70 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)    
    frame:
        xpos 273
        ypos 260
        xpadding 5
        ypadding 15        
        add g.make_button("cgeight",  "cg 80 t", "gui/cglock.png", "cg 80 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 517
        ypos 260
        xpadding 5
        ypadding 15        
        add g.make_button("cgnine",  "cg 90 t", "gui/cglock.png", "cg 90 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 759
        ypos 260
        xpadding 5
        ypadding 15        
        add g.make_button("cgten",  "cg 100 t", "gui/cglock.png", "cg 100 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)

#Duplicate for now
screen mygallery2:
    
    tag menu

    use cgnavigation

    frame:
        background None
        foreground "gallerythis"
    frame:
        xpos 31
        ypos 60
        xpadding 5
        ypadding 15
        add g.make_button("cgeleven", "cg 110 t", "gui/cglock.png", "cg 110 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 273
        ypos 60
        xpadding 5
        ypadding 15
        add g.make_button("cge2", "cg e2 t", "gui/cglock.png", "cg e2 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 517
        ypos 60
        xpadding 5
        ypadding 15        
        add g.make_button("cge3", "cg e3 t", "gui/cglock.png", "cg e3 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 759
        ypos 60
        xpadding 5
        ypadding 15        
        add g.make_button("cgb2",  "cg b2 t", "gui/cglock.png", "cg b2 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 31
        ypos 260
        xpadding 5
        ypadding 15        
        add g.make_button("cgb3", "cg b3 t", "gui/cglock.png", "cg b3 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)    
    frame:
        xpos 273
        ypos 260
        xpadding 5
        ypadding 15        
        add g.make_button("traincgs",  "alicesing t", "gui/cglock.png", "alicesing c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 517
        ypos 260
        xpadding 5
        ypadding 15        
        add g.make_button("cgnine",  "cg 90 t", "gui/cglock.png", "cg 90 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    frame:
        xpos 759
        ypos 260
        xpadding 5
        ypadding 15        
        add g.make_button("cgnine",  "cg 90 t", "gui/cglock.png", "cg 90 c", xanchor = 0, yanchor = 0, xalign = 0, yalign = 0, xpos = 0, ypos = 0, xmargin = 0, ymargin = 0, background = None)
    

init python:        
    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=2.0)

    # Step 2. Add music files.

  
    mr.add("music/titlestart.ogg", always_unlocked=True)
    mr.add("music/titleloop.ogg", always_unlocked=True)
    mr.add("music/silly.ogg", always_unlocked=True)
    mr.add("music/SparklyDayIntro.ogg", always_unlocked=True)     
    mr.add("music/SparklyDay.ogg", always_unlocked=True)      
    mr.add("music/AliceBalladbad.ogg", always_unlocked=True)
    mr.add("music/AliceBalladgood.ogg", always_unlocked=True)
    mr.add("music/AlicePopbad.ogg", always_unlocked=True)
    mr.add("music/AlicePopgood.ogg", always_unlocked=True)  
    mr.add("music/AliceRockbad.ogg", always_unlocked=True)
    mr.add("music/AliceRockgood.ogg", always_unlocked=True)     
    mr.add("music/nightsintro.ogg", always_unlocked=True)
    mr.add("music/nightsloop.ogg", always_unlocked=True)    
    mr.add("music/kissingintro.ogg", always_unlocked=True)  
    mr.add("music/kissingloop.ogg", always_unlocked=True)
    mr.add("music/babysoft.ogg", always_unlocked=True)
    mr.add("music/dining.ogg", always_unlocked=True)  
    mr.add("music/gameplaystart.ogg",always_unlocked=True)
    mr.add("music/gameplayloop.ogg", always_unlocked=True)    
    mr.add("music/gameplayend.ogg", always_unlocked=True)  
    
screen mymusic:

    tag menu

    use cgnavigation

    frame:
        background "gui/softpink.png"
        ypos 80
        foreground "jukethis"
    grid 2 1:    
        xalign 0.5
        yalign 0.2
        vbox:
            #background None
            xalign 0.1 
            #yalign 0.5

        # The buttons that play each track.
            textbutton _("{font=AtomicClockRadio.ttf}01 Reflections{/font}"):
                background None
                action (Play("music", "music/titlestart.ogg"), Queue("music", "music/titleloop.ogg"))
            textbutton _("{font=AtomicClockRadio.ttf}02 Clowning Around{/font}"):
                background None
                action mr.Play("music/silly.ogg")
            textbutton _("{font=AtomicClockRadio.ttf}03 Sparkly Day{/font}"):
                background None
                action (Play("music", "music/SparklyDayIntro.ogg"), Queue("music", "music/SparklyDay.ogg"))      
            textbutton _("{font=AtomicClockRadio.ttf}04 Rising Star - Amateur{/font}"):
                background None
                action mr.Play("music/AliceBalladbad.ogg")
            textbutton _("{font=AtomicClockRadio.ttf}05 Rising Star - Promix{/font}"):
                background None
                action mr.Play("music/AliceBalladgood.ogg")
            textbutton _("{font=AtomicClockRadio.ttf}06 One Step Forward - Amateur{/font}"):
                background None
                action mr.Play("music/AlicePopbad.ogg")
            textbutton _("{font=AtomicClockRadio.ttf}07 One Step Forward - Promix{/font}"):
                background None
                action mr.Play("music/AlicePopgood.ogg")
           

        vbox:
            xalign 0.9 
            #yalign 0.5                
            #background None  
            textbutton _("{font=AtomicClockRadio.ttf}08 Rock the Idol - Amateur{/font}"):
                background None
                action mr.Play("music/AliceRockbad.ogg")
            textbutton _("{font=AtomicClockRadio.ttf}09 Rock the Idol - Promix{/font}"):
                background None
                action mr.Play("music/AliceRockgood.ogg")                 
            textbutton _("{font=AtomicClockRadio.ttf}10 Moonglow{/font}"):
                background None
                action (Play("music", "music/nightsintro.ogg"), Queue("music", "music/nightsloop.ogg"))          
            textbutton _("{font=AtomicClockRadio.ttf}11 Moment of Bliss{/font}"):
                background None
                action (Play("music", "music/kissingintro.ogg"), Queue("music", "music/kissingloop.ogg"))
            textbutton _("{font=AtomicClockRadio.ttf}12 Alice's Lullaby{/font}"):
                background None
                action mr.Play("music/babysoft.ogg")
            textbutton _("{font=AtomicClockRadio.ttf}13 A Night Out{/font}"):
                background None
                action mr.Play("music/dining.ogg")
            textbutton _("{font=AtomicClockRadio.ttf}14 Sunshine Idol{/font}"):
                background None
                action (Play("music", "music/gameplaystart.ogg"), Queue("music", "music/gameplayloop.ogg"), Queue("music", "music/gameplayend.ogg"))
                
    frame:
        background None
        xalign 0.5
        ypos 350
        has hbox:
            xalign 0.5
            yalign 0.5
             
        # Buttons that let us advance tracks.
        textbutton _("{font=AtomicClockRadio.,ttf}|<<{/font}"):
            #background None
            action mr.Previous() 
        textbutton _("{font=AtomicClockRadio.,ttf}>>|{/font}"):
            #background None
            action mr.Next()

        
    # Start the music playing on entry to the music room.
#    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
#    on "replaced" action Play("music", "sounds/title.gg")

