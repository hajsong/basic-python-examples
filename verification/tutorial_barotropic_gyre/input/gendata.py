#!/usr/bin/env python
def gendata():
  """
    Generate MITgcm tutorial_barotropic_gyre input files

    Outputs:
     topog.box:    Domain depths ( m       )
     windx.sin_y:  Wind stress   ( Nm^{-2} )
  """

  import numpy as np

  # Set ouput I/O to double precision IEEE big endian,
  # the MITgcm default.
  ofmt = '>f8'

  # Domain depth and size in X and Y grid points.
  Ho = 5000
  nx = 60
  ny = 60

  # Generate bathymetry with flat bottom at z=-Ho
  h = -Ho*np.ones([nx, ny])
  # Walls
  h[-1, :] = 0
  h[:, -1] = 0
  with open('topog.box','wb') as fid:
    h.astype(ofmt).tofile(fid,"") 

  # Generate zonal wind-stress file that is sin with period of dmain north-south extent
  # and maximum of 0.1 Nm^{2}
  tauMax = 0.1
  x = (np.arange(1,nx+1)-0.5) / (nx-1.) # nx-1 accounts for a solid wall
  y = (np.arange(1,ny+1)-0.5) / (ny-1.) # ny-1 accounts for a solid wall
  X, Y = np.meshgrid(x,y)
  tau = tauMax*np.sin(np.pi*Y)
  with open('windx.sin_y','wb') as fid:
    tau.astype(ofmt).tofile(fid,"") 

if __name__ == '__main__':
 gendata()
