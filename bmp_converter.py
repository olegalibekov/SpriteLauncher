from PIL import Image, ImageDraw
import cv2
# img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))
#
# draw = ImageDraw.Draw(img)
# draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))
#
# img.save('test.gif', 'GIF', transparency=0)

def convert_to_bmp():
    Image.open('/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighRes.png').save('/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighRes.bmp')

    # Image.open('/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighRes.png').convert('CMYK').save('/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighRes.bmp')

    # img = cv2.imread('/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighRes.png')
    # img_bmp = None
    # img.convertTo(img_bmp, cv2.CV_8UC3)
    # cv2.imwrite('/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighResTransparency.bmp', img_bmp)

    # Mat image = imread("fruit.png", -1);
    # Mat image_bmp;
    # image.convertTo(image_bmp, CV_8UC3);
    # imwrite("fruit.bmp", image_bmp);

    # import subprocess
    # subprocess.call("convert /home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighRes.png /home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighRes.bmp", shell=True)

    # img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))
    # img = Image.open('/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighRes.png')
    # draw = ImageDraw.Draw(img)
    # draw.ellipse((0, 0, 0, 0), fill=(255, 0, 0))
    #
    # img.save('/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighResTransparency.bmp', "bmp", transparency=1)


    # img = Image.open('/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighRes.png')
    # img = img.convert("RGBA")
    # datas = img.getdata()
    #
    # newData = []
    # for item in datas:
    #     if item[0] == 0 and item[1] == 0 and item[2] == 0:
    #         newData.append((256, 256, 256,  0))
    #     else:
    #         newData.append(item)
    #
    # img.putdata(newData)
    # img.save("/home/fehty/Pictures/object13494_Folding_Chairs_v1_L3_036HighResTransparency.bmp", "bmp", transparency=1)
