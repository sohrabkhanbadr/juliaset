import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def julia_set(c, im_width, im_height, nit_max, zabs_max):
  """
  Calculates the Julia set for a given complex number 'c'.

  Args:
      c: The complex number parameter.
      im_width: The width of the image.
      im_height: The height of the image.
      nit_max: The maximum number of iterations.
      zabs_max: The escape radius.

  Returns:
      A NumPy array representing the Julia set.
  """
  xmin, xmax = -2.0, 2.0
  ymin, ymax = -2.0, 2.0
  xwidth = xmax - xmin
  yheight = ymax - ymin
  julia = np.zeros((im_height, im_width))

  for ix in range(im_width):
    for iy in range(im_height):
      nit = 0
      z = complex(ix / im_width * xwidth + xmin, iy / im_height * yheight + ymin)
      while abs(z) <= zabs_max and nit < nit_max:
        z = z * z + c
        nit += 1
      ratio = nit / nit_max
      julia[ix, iy] = ratio

  return julia

# Example usage:
c = complex(-0.1, 0.65)
im_width, im_height = 500, 500
nit_max = 128
zabs_max = 2.0

julia_set_data = julia_set(c, im_width, im_height, nit_max, zabs_max)

# Display the Julia set:
fig, ax = plt.subplots()
ax.imshow(julia_set_data, interpolation='nearest', cmap=cm.hot)
plt.show()
