# Here is the code for our robomaster main assignment. Bulk done by Matthew Verge. Person room Room 3 done by Emily Warford. Fire room room 1 done by Ashley Legge. Measurements, moral support, and help from Cameron Beanland and Princess Bazunu.
# 04/05/2024


# lets do this
robot_ctrl.set_mode(rm_define.robot_mode_free)
led_ctrl.set_top_led(rm_define.armor_top_all, 100, 0, 100, rm_define.effect_marquee)

# fire person functions
def dance_for_them():
    chassis_ctrl.set_rotate_speed(120)
    led_ctrl.set_top_led(rm_define.armor_top_all, 100, 200, 0, rm_define.effect_marquee)
    media_ctrl.play_sound(rm_define.media_custom_audio_2, wait_for_complete=False)
    time.sleep(10)
    chassis_ctrl.move_with_distance(90, .5)
    chassis_ctrl.move_with_distance(-90, .5)
    chassis_ctrl.move_with_distance(-90, .5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 360)
    chassis_ctrl.move_with_distance(90, .5)
    chassis_ctrl.move_with_distance(90, .5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 360)
    chassis_ctrl.move_with_distance(-90, .5)
    chassis_ctrl.move_with_distance(-90, .5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 360)
    chassis_ctrl.move_with_distance(90, .5)
    chassis_ctrl.move_with_distance(90, .5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 360)
    chassis_ctrl.move_with_distance(-90, .5)
    chassis_ctrl.move_with_distance(-90, .5)
    chassis_ctrl.move_with_distance(90, .5)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 1440)
    chassis_ctrl.set_rotate_speed(30)
    time.sleep(1)
    gimbal_ctrl.set_rotate_speed(120)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,40)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,40)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,40)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,40)
    gimbal_ctrl.recenter()
    led_ctrl.set_top_led(rm_define.armor_top_all, 100, 0, 100, rm_define.effect_marquee)

    
    time.sleep(5)

def scan_for_marker():
    
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.yaw_ctrl(-90)
    gimbal_ctrl.yaw_ctrl(90)

def vision_recognized_marker_letter_F(msg):
    gun_ctrl.fire_once()
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)

# person room functions
def scan_for_person():

 vision_ctrl.enable_detection(rm_define.vision_detection_people)
 gimbal_ctrl.yaw_ctrl(90)
 gimbal_ctrl.yaw_ctrl(-0)




def vision_recognized_people(msg):
 media_ctrl.play_sound(rm_define.media_custom_audio_3)
 vision_ctrl.disable_detection(rm_define.vision_detection_people)
 print("detected")
 gimbal_ctrl.recenter()
 time.sleep(2)





# 1 = fire
# 2 = poison
# 3 = person

def start():
    room1Type = 3
    room2Type = 1
    room3Type = 2

    
    chassis_ctrl.set_trans_speed(0.6)
    # starting position to end of B
    

    media_ctrl.play_sound(rm_define.media_custom_audio_5, wait_for_complete=True)
    media_ctrl.play_sound(rm_define.media_custom_audio_6, wait_for_complete=True)
    
    
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.move_with_distance(0,5)
    chassis_ctrl.move_with_distance(0,0.86)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 85)
    chassis_ctrl.move_with_distance(0, 0.80)                    
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 85)
    chassis_ctrl.move_with_distance(0, 0.353)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(1,1.65)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0,.42)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, .52)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
    chassis_ctrl.move_with_distance(0, 1.47)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 51)
    chassis_ctrl.move_with_distance(0,.57)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, .82)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 85)
    chassis_ctrl.move_with_distance(0,.45)

    #reset point
    time.sleep(5)

    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 1.553)
    

    #first room
    if room1Type == 1:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0,2.2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        chassis_ctrl.move_with_distance(0, 2.3)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)        
        scan_for_marker()
        # it should fire
        time.sleep(1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 93)
        chassis_ctrl.move_with_distance(0, 2.3)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        chassis_ctrl.move_with_distance(0, 2.2)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 96) 

    elif room1Type == 2:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)
        time.sleep(2)
        media_ctrl.play_sound(rm_define.media_custom_audio_1)
        time.sleep(2)


    elif room1Type == 3:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_always_on)
        vision_ctrl.set_marker_detection_distance(1.0)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,2.3)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,2.3)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        scan_for_person()

        time.sleep(1)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,2.3)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

        chassis_ctrl.move_with_distance(0,2.3)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 85)

        #move to a and then return

        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,0.86)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.553)
        chassis_ctrl.move_with_distance(0, 2.5)
        time.sleep(1)
        media_ctrl.play_sound(rm_define.media_custom_audio_4)
        time.sleep(1)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        time.sleep(4)
        chassis_ctrl.move_with_distance(0,5)
        chassis_ctrl.move_with_distance(0,0.86)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.553)
        chassis_ctrl.move_with_distance(0, 2.5)
        time.sleep(1)



        

        


    # after returning, continue
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, .232)

    #reset point
    time.sleep(5)
    chassis_ctrl.move_with_distance(0, 4.93)


    if room2Type == 1:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
        vision_ctrl.set_marker_detection_distance(3.0)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,2.6)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,1.6)
 

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 86)

        chassis_ctrl.move_with_distance(0,4.5)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,1.0)
 
        scan_for_marker()

        time.sleep(2)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

        chassis_ctrl.move_with_distance(0,1.0)


        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 86)

        chassis_ctrl.move_with_distance(0,4.5)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,1.6)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

        chassis_ctrl.move_with_distance(0,2.3)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        
    
    elif room2Type == 2:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)
        time.sleep(2)
        media_ctrl.play_sound(rm_define.media_custom_audio_1)
        time.sleep(2)

    elif room2Type == 3:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_always_on)
        robot_ctrl.set_mode(rm_define.robot_mode_free)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,2.6)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,1.6)
 

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 86)

        chassis_ctrl.move_with_distance(0,4.5)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,0.3)
 

        scan_for_person()

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

        chassis_ctrl.move_with_distance(0,0.3)


        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 87)

        chassis_ctrl.move_with_distance(0,4.5)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)

        chassis_ctrl.move_with_distance(0,1.7)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

        chassis_ctrl.move_with_distance(0,2.6)

        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 86)
        #return to a, return to room 2

        chassis_ctrl.move_with_distance(0, 5.0)
        time.sleep(5)

        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 1.3)
        chassis_ctrl.move_with_distance(0, 5)
        
        time.sleep(5)
        
        chassis_ctrl.move_with_distance(0, 3.353)
        chassis_ctrl.move_with_distance(0, 5.0)
        
        time.sleep(1)
        media_ctrl.play_sound(rm_define.media_custom_audio_4)
        time.sleep(1)

        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)

        chassis_ctrl.move_with_distance(0, 3.353)
        chassis_ctrl.move_with_distance(0, 5.0)
        time.sleep(5)

        

        chassis_ctrl.move_with_distance(0, 5.0)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 1.353)
        time.sleep(5)

        chassis_ctrl.move_with_distance(0, 5.0)
        time.sleep(3)


    
    chassis_ctrl.move_with_distance(0, 4.0)
    
    #reset point
    time.sleep(5)
 
    
    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, .08)

    # person room marker 3 (notice sign 3, scan for person, return to A)

    if room3Type == 1:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
        
    
    elif room3Type == 2:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)
        time.sleep(2)
        media_ctrl.play_sound(rm_define.media_custom_audio_1)
        time.sleep(2)

    elif room3Type == 3:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 255, rm_define.effect_always_on)

    chassis_ctrl.move_with_distance(0, 5.0)
    chassis_ctrl.move_with_distance(0, .105)



    # return to a

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    time.sleep(5)
    chassis_ctrl.set_trans_speed(1.0)
    chassis_ctrl.move_with_distance(0, 5.0)

    chassis_ctrl.move_with_distance(0, .105)

    chassis_ctrl.move_with_distance(0, 5.0)

    chassis_ctrl.move_with_distance(0, 0.08)
    
    time.sleep(5)

    chassis_ctrl.move_with_distance(0, 3.759)

    chassis_ctrl.move_with_distance(0, 4.93)
    time.sleep(5)
    
    dance_for_them()

    chassis_ctrl.move_with_distance(0, 5.00)

    chassis_ctrl.move_with_distance(0, 5.00)
    
    chassis_ctrl.move_with_distance(0, 1.3)

    time.sleep(5)

    

    chassis_ctrl.move_with_distance(0, 5.00)

    chassis_ctrl.move_with_distance(0, 3.6)

    # moving back to A!
    time.sleep(2)
    #victory music

    media_ctrl.play_sound(rm_define.media_sound_solmization_2C)
    time.sleep(0.2)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2C)
    time.sleep(0.2)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2C)
    time.sleep(0.2)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2C)
    time.sleep(0.3)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1GSharp)
    time.sleep(0.5)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1ASharp)
    time.sleep(0.4)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2C)
    time.sleep(0.3)
    media_ctrl.play_sound(rm_define.media_sound_solmization_1ASharp)
    time.sleep(0.2)
    media_ctrl.play_sound(rm_define.media_sound_solmization_2C)
    time.sleep(3)
    # end
