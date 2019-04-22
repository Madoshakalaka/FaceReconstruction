import os
import traceback

import numpy as np
from skimage.io import imread
from skimage.transform import rescale

from api import PRN
from utils.write import write_obj_with_colors

# ---- init PRN
os.environ['CUDA_VISIBLE_DEVICES'] = '0' # GPU number, -1 for CPU
prn = PRN(is_dlib = True)


save_folder = '/home/matt/PycharmProjects' \
              '/webtest/mysite/modelEvalMedia'




# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345


s.bind(('localhost', port))
print "socket binded to %s" % (port)

# put the socket into listening mode
s.listen(5)
print "socket is listening"

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.

    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    print 'Got connection from', addr

    # send a thank you message to the client.
    filename = c.recv(1024).decode('utf-8')
    print(filename)

    try:


        image_path = '/home/matt/' \
                     'PycharmProjects/' \
                     'webtest/mysite' + filename


        image = imread(image_path)

        [h, w, cc] = image.shape
        if cc>3:
            image = image[:,:,:3]


        max_size = max(image.shape[0], image.shape[1])
        if max_size > 1000:
            image = rescale(image, 1000. / max_size)
            image = (image * 255).astype(np.uint8)


        pos = prn.process(image)

        image = image / 255.
        if pos is None:
            raise Exception()

        kpt = prn.get_landmarks(pos)
        # 3D vertices
        vertices = prn.get_vertices(pos)
        save_vertices = vertices.copy()
        save_vertices[:, 1] = image.shape[0] - 1 - save_vertices[:, 1]

        # corresponding colors
        colors = prn.get_colors(image, vertices)

        name = image_path.strip().split('/')[-1][:-4]

        write_obj_with_colors(os.path.join(save_folder, name + '.obj'),
                              save_vertices, prn.triangles, colors)


    except:
        traceback.print_exc()
        c.send("problem occurred during reconstruction".encode('utf-8'))
    else:
        c.send(name.encode('utf-8'))


    # Close the connection with the client
    c.close()