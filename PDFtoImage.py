from __future__ import print_function
from wand.image import Image

# with Image(filename='990-form-stjude-fy15.pdf') as img:
#     print('pages = ', len(img.sequence))
 
#     with img.convert('jpg') as converted:
#         converted.save(filename='page.png')
        
from wand.image import Image
from wand.display import display

with Image(filename='990-form-stjude-fy15.pdf') as img:
    print(img.size)
    for r in 1, 2, 3:
        with img.clone() as i:
            i.resize(int(i.width * r * 1), int(i.height * r * 1))
            i.rotate(90 * r)
            i.save(filename='990-form-stjude-fy15.pdf'.format(r))
            display(i)
        