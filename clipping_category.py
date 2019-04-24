from PIL import Image, ImageChops
import glob, os

def clipping(fname, original, segment, color):
    img = Image.open(segment).convert('RGB')
    r, g, b = img.split()

    _r = r.point(lambda _: 1 if _ == color[0] else 0, mode="1")
    _g = g.point(lambda _: 1 if _ == color[1] else 0, mode="1")
    _b = b.point(lambda _: 1 if _ == color[2] else 0, mode="1")

    mask = ImageChops.logical_and(_r, _g)
    mask = ImageChops.logical_and(mask, _b)

    ori_img = Image.open(original)
    ori_img.putalpha(mask)
    ori_img.save(fname)


color = {
    'back':(0,0,0),
    'socks':(255,0,0),
    'skirt':(0,255,0),
    'clothes':(0,0,255),
    'skin':(255,255,0),
    'shoes':(255,0,255),
    'face':(0,255,255),
    'hair':(128,128,128),
    'accessories':(128,128,0)
}

if __name__ == "__main__":
    segment = glob.glob('.\\segment\\*')

    for i in segment:
        ori_dir = '.\\original\\' + i.split('\\', 2)[-1]

        dire = i.split('\\')[-1].split('.')[0]
        for key, val in color.items():
            fname = f'./clipping/{dire}/{key}.png'
            os.makedirs(f'./clipping/{dire}', exist_ok=True)
            clipping(fname, ori_dir, i, val)