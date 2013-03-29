import cv
from lib import track,x
def main():
    old_center=None
    capture=cv.CaptureFromCAM(0)
    cv.NamedWindow("jarvis")
    #Click on named window and obtain its color using this callback
    #cv.SetMouseCallback("jarvis",x.get_clicked_color,cv.QueryFrame(capture))
    while(1):
        color_image,data=track.track_data(cv.QueryFrame(capture))
        data=track.filter_fingers(data)
        #Optimize mouse center based on previous data before moving mouse
        optimized_centerX,optimized_centerY=track.optimize_mouse_center(old_center,data.center)
        if(optimized_centerX and optimized_centerY):
            x.mouse_move(optimized_centerX,optimized_centerY)
            old_center=data.center
            #try:
                #if((data.center['x'] not in range(old_center['x']-5,old_center['x']+5)) and (data.center['x'] not in range(old_center['x']-5,old_center['x']+5))):
                    #x.mousemove((data.center['x']*1380)/640,(data.center['y']*800)/480)
                    #old_center=data.center
            #except:
                #old_center=data.center
        cv.ShowImage("jarvis",color_image)
        if cv.WaitKey(33)==1048603:
            cv.DestroyWindow("jarvis")
            exit()

if __name__=='__main__':
    main()