import project
def create(a,b):
    out =[]
    for x in range(b):
        row =[]
        for y in range(a):
            red=x//2%256
            green=y//2%256
            blue=(x//2*y//2)%256
            pixel=[red,green,blue]
            row.append(pixel)
        out.append(row)
    return out

image=create(20,20)

def writePPM(image,filename):
    height=len(image)
    width=len(image[0])
    f = open(filename,"w")
    f.write("P3\n")
    f.write(str(width)+" "+str(height)+"\n")
    f.write("255\n")
    for y in range(len(image)):
        for x in range(len(image[y])):
            for c in range(len(image[y][x])):
                f.write(str(image[y][x][c])+" ")
    f.write("\n")
    f.close()
    
def main():
    #smilely face
    shapes=project.createSmileyFace()
    circles=project.getCircles(shapes)
    rectangles=project.getRectangles(shapes)
    pixelList=[]
    project.processCircles(circles,pixelList)
    project.processRectangles(rectangles,pixelList)
    project.orderPixels(pixelList)
    image=project.createImage([255,255,0],200,200)
    project.drawPixels(image,pixelList)


    writePPM(image,"smile.ppm")
    #circles
    shapes=[]
    for x in range(255):
        shapes.append(project.createCircle(0,x,0,100,75+x,50,-x))
    circles=project.getCircles(shapes)

    pixelList=[]
    project.processCircles(circles,pixelList)
    image=project.createImage([255,255,0],200,400)
    project.drawPixels(image,pixelList)
    writePPM(image,"circles1.ppm")

    project.orderPixels(pixelList)
    image=project.createImage([255,255,0],200,400)
    project.drawPixels(image,pixelList)
    writePPM(image,"circles2.ppm")

main()



