from time import sleep
from moving_arms import waving_arms
from Object_Detection_Files import detect_bird
import buzzer_run


def MainRnn():

    #taking pictures and detect bird
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
        

    
    
if __name__ == "__main__":
    MainRnn()

