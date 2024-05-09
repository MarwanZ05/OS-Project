import math
import pygame
 
def main():
    # Input, process & validate burst times
    burst_times = input("Input burst times:").split(" ")
    burst_times = [int(x) for x in burst_times]
    for x in burst_times: 
        if x <=  0: 
            print("Error: cannot enter zero or a negative number.")
            return
        
    # Convert to an array of tuples where a tuple is (process ID, burst time)
    burst_times_sum = sum(burst_times)
    burst_times = [(i,burst_times[i]) for i in range(len(burst_times))]
    # sort array
    burst_times.sort(key = lambda x : x[1])
    waiting_time = 0
    for i in range(len(burst_times)):
        # add waiting time and completion time to tuple
        #      proc num, burst  ,waiting,  completion
        # Waiting time = total burst times before this process
        burst_times[i] = (burst_times[i][0],burst_times[i][1],waiting_time,waiting_time+burst_times[i][1])
        # increment time
        waiting_time += burst_times[i][1]
    # print stuff
    print(burst_times)
    print(burst_times_sum)
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("Shortest Job First (Non-preemptive)")
    # create a surface on screen that has the size of 800 x 600
    screen = pygame.display.set_mode((800,600))
     
    # fill background
    screen.fill((255,255,255))
    
    # load font, prepare values
    font = pygame.font.Font(None, 16)

    # draw background of gantt chart
    pygame.draw.rect(screen,(200,200,200),(50,50,700,100))
    # draw border of gantt chart
    pygame.draw.rect(screen,(10,10,10),(50,50,700,100),3)
    # loop over processes
    for x in burst_times:
        # calculate start of rectangle
        start = math.floor(get_process_width(x[2],burst_times_sum,700))
        # calculate width of rectangle
        w = math.floor(get_process_width(x[1],burst_times_sum,700))
        # draw border rectngle
        pygame.draw.line(screen,(10,20,10),(50+start+w,50),(50+start+w,149),3)
        # write process number
        #                  text          AA   color
        ren = font.render("P"+str(x[0]), 1, (0,0,0))
        screen.blit(ren, (50+start+w/2-ren.get_width()/2, 100-ren.get_rect().height/2))
        # write start time
        ren = font.render(str(x[2]), 1, (0,0,0))
        screen.blit(ren, (50+start-ren.get_width()/2, 150))
        # write end time
        ren = font.render(str(x[2]+x[1]), 1, (0,0,0))
        screen.blit(ren, (50+start+w-ren.get_width()/2, 150))

    # draw 5 rectangles for table heading
    pygame.draw.rect(screen,(10,20,10),(50,200,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(147,200,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(244,200,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(341,200,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(438,200,100,30),3)
    # write table header
    ren = font.render("Process", 1, (0,0,0))
    screen.blit(ren, (50+50-ren.get_width()/2, 210))
    ren = font.render("Burst Time", 1, (0,0,0))
    screen.blit(ren, (147+50-ren.get_width()/2, 210))
    ren = font.render("Waiting Time", 1, (0,0,0))
    screen.blit(ren, (244+50-ren.get_width()/2, 210))
    ren = font.render("Turnaround Time", 1, (0,0,0))
    screen.blit(ren, (341+50-ren.get_width()/2, 210))
    ren = font.render("Response Time", 1, (0,0,0))
    screen.blit(ren, (438+50-ren.get_width()/2, 210))

    # loop over processes
    for i in range(len(burst_times)):
        # set the y position or at what height to draw
        y = 227+27*i
        # draw 5 rectangles for table borders
        pygame.draw.rect(screen,(50,70,50),(50,y,100,30),3)
        pygame.draw.rect(screen,(50,70,50),(147,y,100,30),3)
        pygame.draw.rect(screen,(50,70,50),(244,y,100,30),3)
        pygame.draw.rect(screen,(50,70,50),(341,y,100,30),3)
        pygame.draw.rect(screen,(50,70,50),(438,y,100,30),3)
        #write table contents
        ren = font.render("P"+str(burst_times[i][0]), 1, (0,0,0))
        screen.blit(ren, (50+50-ren.get_width()/2, y+10))
        ren = font.render(str(burst_times[i][1]), 1, (0,0,0))
        screen.blit(ren, (147+50-ren.get_width()/2, y+10))
        ren = font.render(str(burst_times[i][2]), 1, (0,0,0))
        screen.blit(ren, (244+50-ren.get_width()/2, y+10))
        ren = font.render(str(burst_times[i][3]), 1, (0,0,0))
        screen.blit(ren, (341+50-ren.get_width()/2, y+10))
        ren = font.render(str(burst_times[i][2]), 1, (0,0,0))
        screen.blit(ren, (438+50-ren.get_width()/2, y+10))

    # set y of the last row
    y = 227+27*len(burst_times)
    # draw borders of last row
    pygame.draw.rect(screen,(10,20,10),(50,y,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(147,y,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(244,y,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(341,y,100,30),3)
    pygame.draw.rect(screen,(10,20,10),(438,y,100,30),3)
    # write contents of last row
    ren = font.render("Average", 1, (0,0,0))
    screen.blit(ren, (50+50-ren.get_width()/2, y+10))
    ren = font.render(str(round(sum([x[1] for x in burst_times])/len(burst_times),2)), 1, (0,0,0))
    screen.blit(ren, (147+50-ren.get_width()/2, y+10))
    ren = font.render(str(round(sum([x[2] for x in burst_times])/len(burst_times),2)), 1, (0,0,0))
    screen.blit(ren, (244+50-ren.get_width()/2, y+10))
    ren = font.render(str(round(sum([x[3] for x in burst_times])/len(burst_times),2)), 1, (0,0,0))
    screen.blit(ren, (341+50-ren.get_width()/2, y+10))
    ren = font.render(str(round(sum([x[2] for x in burst_times])/len(burst_times),2)), 1, (0,0,0))
    screen.blit(ren, (438+50-ren.get_width()/2, y+10))

    # display stuff
    pygame.display.flip()

    # define a variable to control the main loop
    running = True
    # main loop(which currently does nothing other than keep the window open)
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type ==  pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

# calculate pixel width of given time   
def get_process_width(burst_time:int,total_time:int,total_width:int):
    return (burst_time/float(total_time))*total_width


if __name__ == "__main__":
    main()