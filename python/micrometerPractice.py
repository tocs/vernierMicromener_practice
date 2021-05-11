import Image, ImageDraw
import sys



def micrometerReading(length,
                      sleeveFile = "./vernierScales_sleeveImg.png",
                      sleeveEnds = [250, 4250],
                      sleeveRange = [0.0, 1.0],
                      thimbleFile = "./vernierScales_thimbleImg.png",
                      thimbleRange = [0, 0.0250],
                      thimbleYZero = 2068,
                      thimbleEnds = [2068.0, 68.0],
                      ):

    def sleeveStuff(): #, sleeveYZero):
        sleevePoint = [sleevePosition(length), sleeveYZero]
        pic = ImageDraw.Draw(sleeveImg)
        pic.ellipse([sleevePoint[0] - 10, sleevePoint[1] - 10, sleevePoint[0] + 10, sleevePoint[1] + 10], fill = (255,0,0))
        del pic
        return(sleevePoint)

    def thimbleStuff():
        pic = ImageDraw.Draw(thimbleImg)
        pic.ellipse([thimblePoint[0] - 10, thimblePoint[1] - 10, thimblePoint[0] + 10,
                     thimblePoint[1] + 10], fill = (255,0,0))
        del pic
        sleeveImg.paste(thimbleImg,
                        (int(sleevePoint[0]),
                         int(sleeveYZero - thimblePoint[1])))

        # if thimble image does not fill top of image past copy above
        if (int(sleeveYZero - thimblePoint[1]) > 0) and (int(sleeveYZero - thimblePoint[1]) < sleeveImg.size[1]):
            sleeveImg.paste(thimbleImg,
                            (int(sleevePoint[0]),
                             136 + int(sleeveYZero - thimblePoint[1]) - thimbleImg.size[1]))
        # if thimble image does not fill bottom of image past copy below
        if thimbleImg.size[1] + int(sleeveYZero - thimblePoint[1]) < sleeveImg.size[1]:
            sleeveImg.paste(thimbleImg,
                            (int(sleevePoint[0]),
                             int(sleeveYZero - thimblePoint[1]) + thimbleImg.size[1] - 136))


    
    sleevePosition = (lambda length: sleeveEnds[0] + length * ( sleeveEnds[1] - sleeveEnds[0]))
    thimblePosition = (lambda pos: thimbleEnds[0] - ((pos % 0.025) * (thimbleEnds[0] - thimbleEnds[1])) / 0.025)
    thimbleImg = Image.open(thimbleFile)
    sleeveImg = Image.open(sleeveFile)
    thimblePoint = [0, thimblePosition(length)]
    sleeveYZero = sleeveImg.size[1] - 820.0
    sleevePoint = sleeveStuff()
    thimbleStuff()
    sleeveImg.save("test%f.png" % length)

if __name__ == "__main__":

    args = sys.argv
    if len(args) > 1:
        length = float(args[-1])
    else:
        length = 0.5000

    micrometerReading(length)
