from PIL import Image
import glob
import os

pth_screens = os.path.realpath( "./screens" )
pth_out = os.path.realpath( "./textures" )

def save_image( im, index ):
    im.save(
        os.path.join(
            pth_out,
            "bars{:d}.png".format(index)
        )
    )

num_textures = 10
texture_width = 4

im_count = 0
for i, fn_screen in enumerate(glob.glob( os.path.join(pth_screens,"*.tif" ))):

    if i >= num_textures:
        break

    pth_screen = os.path.join( pth_screens, fn_screen )

    print( pth_screen )

    im = Image.open( pth_screen )

    # resize image
    sz = im.size
    im_h = sz[1]
    im = im.resize( (texture_width,im_h) )

    top_h = int(im_h/2)


    # box – The crop rectangle, as a (left, upper, right, lower)-tuple.
    box = (0,0,texture_width,top_h)
    top = im.crop( box )

    save_image( top, im_count )
    
    im_count += 1

    box = (0,top_h,texture_width,im_h)
    bottom = im.crop( box )

    save_image( bottom, im_count )
    
    im_count += 1

