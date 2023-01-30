from time import sleep
import time
from moving_arms import waving_arms
from Object_Detection_Files import detect_bird
import buzzer_run
import sensor_run



def MainRnn():

    #taking pictures and detect bird
    while True:
        sensor_run.setup()
        d = sensor_run.Measure(time)
        print ("distance: ", d)
        
        if d < 20:
            objectinfo = detect_bird.detect()
            print (objectinfo)
    
            #if bird
            if objectinfo:
       
                #buzzer set
                buzzer_run.setup(26) 

                #first turn on buzzer
                buzzer_run.on()
        
                #then waving arms
                waving_arms(sleep)
        
                #off buzzer
                buzzer_run.off()
        #break                
        print ("restart detection....")
        
        time.sleep(3)


    
    
if __name__ == "__main__":
    MainRnn()

